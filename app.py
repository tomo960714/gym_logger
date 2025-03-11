#imports
from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# Pages
@app.route('/')
def index():
    return "Hello World"


# Run the app
if __name__ == '__main__':
    app.run(debug=True)