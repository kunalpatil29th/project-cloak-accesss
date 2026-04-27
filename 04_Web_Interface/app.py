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
from flask import Flask, render_template, Response, jsonify, send_from_directory
import cv2
from datetime import datetime

# Add the parent directory to sys.path to import from utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.db_manager import DBManager
import importlib.util

# Dynamically import InvisibleCloak from the numbered folder
spec = importlib.util.spec_from_file_location("advanced_cloak", os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "03_Advanced", "advanced_cloak.py"))
advanced_cloak = importlib.util.module_from_spec(spec)
spec.loader.exec_module(advanced_cloak)
InvisibleCloak = advanced_cloak.InvisibleCloak

# Initialize the Flask application
app = Flask(__name__)
db = DBManager()
cloak = InvisibleCloak()

# Global variables for session tracking
session_start_time = None

def gen_frames():
    """
    Generator function for video streaming.
    
    Definition: Generator - A special type of function that returns an iterable 
    set of items, one at a time, in a special way.
    """
    global session_start_time
    session_start_time = datetime.now()
    
    if cloak.background is None:
        cloak.capture_background()
    
    try:
        while True:
            success, frame = cloak.cap.read()
            if not success:
                break
            else:
                final_output = cloak.process_frame(frame)
                ret, buffer = cv2.imencode('.jpg', final_output)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    finally:
        # Log session when generator is closed or interrupted
        if session_start_time:
            end_time = datetime.now()
            db.log_session(session_start_time, end_time)
            session_start_time = None

@app.route('/')
def index():
    """
    The index route for the web application.
    
    Definition: Decorator - A design pattern in Python that allows a user to add new 
    functionality to an existing object without modifying its structure.
    """
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """
    Video streaming route. The 'src' attribute of an <img> tag is set to this URL.
    
    Definition: MIME Type - A standard that indicates the nature and format of a document.
    """
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture_background')
def capture_background():
    """
    API endpoint to trigger background capture.
    
    Definition: API Endpoint - A specific URL where an API can be accessed by a 
    client application.
    """
    try:
        cloak.capture_background()
        return jsonify({"status": "success", "message": "Background captured successfully!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/history')
def history():
    """
    Route to display session history from the database.
    """
    sessions = db.get_all_sessions()
    return render_template('history.html', sessions=sessions)

@app.route('/download')
def download():
    """
    Route to download the processed video.
    
    Definition: Static File - A file that is served to the user as-is, such as 
    an image, video, or PDF.
    """
    directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = "output_cloak.mp4"
    return send_from_directory(directory, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
