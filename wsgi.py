import sys
import os

# Add your project directory to the sys.path
project_home = '/home/tomo960714/gym_logger'  # Update this path with your project location
if project_home not in sys.path:
    sys.path.append(project_home)

# Set the Flask app environment variable
from app import create_app
application = create_app()
