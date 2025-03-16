#imports
from flask import Flask, render_template, redirect, request, jsonify, url_for, Blueprint
from app.db import db_sign_up,db_sign_in,db_sign_out
import datetime

app_blueprint=Blueprint("app",__name__)

### Config ###

### Database ###

#Get the Exercises from the database
#For now, a dummy dict is used

exercise_units = {
    "Squat":"kg",
    "Bench Press":"kg",
    "Deadlift":"kg",
    "Overhead Press":"kg",
    "Bike":"km",
    "Run":"km",
    "Swim":"m"
}

### Routes ##
# Pages
@app_blueprint.route('/')
def index():
    return render_template('index.html')

@app_blueprint.route('/input', methods=['GET', 'POST'])
def input():
    current_date = datetime.date.today()
    exercises = list(exercise_units.keys())
    # If the form is submitted
    if request.method == 'POST':
        
        # Get the data from the form
        user = request.form.get("user_select")
        exercise = request.form.get("exercise_select")
        date = request.form.get("date")
        weights = request.form.getlist("weight[]")

        # Debugging: Print values in the console
        print(f"User: {user}")
        print(f"Exercise: {exercise}")
        print(f"Date: {date}")

        # Save the data to the database
        # For now, just print the values
        if weights:
            for weight in weights:
                print(f"Weight: {weight }")

        # Redirect to the input page
        return redirect('/input')
    
    # Render the input page
    return render_template('input.html',exercises=exercises,current_date=current_date)

@app_blueprint.route('/get_unit', methods=['GET'])
def get_unit():
    exercise = request.args.get("exercise", "")
    unit = exercise_units.get(exercise, "kg")  # Default to "kg" if not found
    return jsonify({"unit": unit})  # Return JSON response

@app_blueprint.route('/visuals')
def visuals():
    return render_template('visuals.html')

#TODO: Make login disappear if logged in. Change it to log out.
@app_blueprint.route('/login', methods=['POST','GET'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = db_sign_in(email=email,password=password)
        print(user)
        return redirect(url_for("index"))  # Redirect to home after login
    return render_template("login.html")

@app_blueprint.route('/register',methods=['POST','GET'])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        username = request.form.get("username")
        response = db_sign_up(email=email,password=password)
        print(response)
        return redirect(url_for("app.register_success"))
    return render_template("register.html")
    
@app_blueprint.route('/register/success', methods=['POST',"GET"])
def register_success():
    return render_template("register_success.html")


