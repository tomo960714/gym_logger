#imports
from flask import Flask, render_template, redirect, request, jsonify
import datetime

app = Flask(__name__)

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
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input', methods=['GET', 'POST'])
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

@app.route('/get_unit', methods=['GET'])
def get_unit():
    exercise = request.args.get("exercise", "")
    unit = exercise_units.get(exercise, "kg")  # Default to "kg" if not found
    return jsonify({"unit": unit})  # Return JSON response

@app.route('/visuals')
def visuals():
    return render_template('visuals.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)