#imports
from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# Pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/visuals')
def visuals():
    return render_template('visuals.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)