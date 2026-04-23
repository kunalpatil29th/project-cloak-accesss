"""
Project Cloak Access: 04_Web_Interface - app.py

Definition:
Web Framework: A software framework that is designed to support the development of web 
applications including web services, web resources, and web APIs. Flask is a micro web 
framework written in Python.

Concepts:
1. Routing: The process of determining which code should run when a specific URL is requested.
2. View Function: A Python function that takes a web request and returns a web response.
3. Templates: Files that contain static data as well as placeholders for dynamic data.
"""

import os
import sys
from flask import Flask, render_template, Response
import cv2
from datetime import datetime

# Add the parent directory to sys.path to import from utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.db_manager import DBManager

# Initialize the Flask application
app = Flask(__name__)
db = DBManager()

# Global variables for session tracking
session_start_time = None

@app.route('/')
def index():
    """
    The index route for the web application.
    
    Definition: Decorator - A design pattern in Python that allows a user to add new 
    functionality to an existing object without modifying its structure.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
