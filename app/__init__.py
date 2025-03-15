# app/__init__.py
from flask import Flask
from app.db import Config, supabase
from app.routes import app_blueprint

def create_app():
    app = Flask(__name__)

    # Load configurations
    app.config.from_object(Config)

    # Register blueprints (routes)
    app.register_blueprint(app_blueprint)

    return app