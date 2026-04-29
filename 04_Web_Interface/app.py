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
from flask import Flask, render_template, Response, jsonify, send_from_directory, request
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
is_recording = False

def gen_frames():
    """
    Generator function for video streaming.
    
    Definition: Generator - A special type of function that returns an iterable 
    set of items, one at a time, in a special way.
    """
    global session_start_time, is_recording
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
                
                # Record if enabled
                if is_recording and cloak.video_writer:
                    cloak.video_writer.write(final_output)
                
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
        
        # Stop recording if active
        if is_recording:
            is_recording = False
            if cloak.video_writer:
                cloak.video_writer.release()
                cloak.video_writer = None

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

@app.route('/update_hsv', methods=['POST'])
def update_hsv():
    """
    API endpoint to update HSV color ranges.
    
    Definition: POST Request - An HTTP method used to send data to a server to 
    create/update a resource.
    """
    try:
        data = request.get_json()
        
        # Extract HSV values from request
        lower1 = (data['h1_low'], data['s1_low'], data['v1_low'])
        upper1 = (data['h1_high'], data['s1_high'], data['v1_high'])
        lower2 = (data['h2_low'], data['s2_low'], data['v2_low'])
        upper2 = (data['h2_high'], data['s2_high'], data['v2_high'])
        
        cloak.update_hsv_ranges(lower1, upper1, lower2, upper2)
        return jsonify({"status": "success", "message": "HSV ranges updated!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route('/update_morph', methods=['POST'])
def update_morph():
    """
    API endpoint to update morphological parameters.
    """
    try:
        data = request.get_json()
        kernel_size = (data['kernel_size'], data['kernel_size'])
        dilation_iterations = data['dilation_iterations']
        
        cloak.update_morphological_params(kernel_size, dilation_iterations)
        return jsonify({"status": "success", "message": "Morphological parameters updated!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route('/history')
def history():
    """
    Route to display session history from the database.
    """
    sessions = db.get_all_sessions()
    stats = db.get_statistics()
    return render_template('history.html', sessions=sessions, stats=stats)

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

@app.route('/delete_session/<int:session_id>', methods=['DELETE'])
def delete_session(session_id):
    """
    API endpoint to delete a specific session.
    """
    try:
        success = db.delete_session(session_id)
        if success:
            return jsonify({"status": "success", "message": f"Session {session_id} deleted!"})
        else:
            return jsonify({"status": "error", "message": "Session not found"}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/clear_history', methods=['DELETE'])
def clear_history():
    """
    API endpoint to clear all session history.
    """
    try:
        db.clear_all_sessions()
        return jsonify({"status": "success", "message": "All history cleared!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/start_recording', methods=['POST'])
def start_recording():
    """
    API endpoint to start video recording.
    """
    global is_recording
    try:
        if is_recording:
            return jsonify({"status": "error", "message": "Already recording!"}), 400
        
        # Initialize video writer
        success, frame = cloak.cap.read()
        if not success:
            return jsonify({"status": "error", "message": "Failed to read camera frame"}), 500
        
        # Setup video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        frame_size = (frame.shape[1], frame.shape[0])
        cloak.video_writer = cv2.VideoWriter(
            'output_cloak.mp4',
            fourcc,
            20.0,
            frame_size
        )
        
        is_recording = True
        return jsonify({"status": "success", "message": "Recording started!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/stop_recording', methods=['POST'])
def stop_recording():
    """
    API endpoint to stop video recording.
    """
    global is_recording
    try:
        if not is_recording:
            return jsonify({"status": "error", "message": "Not recording!"}), 400
        
        is_recording = False
        if cloak.video_writer:
            cloak.video_writer.release()
            cloak.video_writer = None
        
        return jsonify({"status": "success", "message": "Recording stopped! Video saved as output_cloak.mp4"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/recording_status')
def recording_status():
    """
    API endpoint to get recording status.
    """
    return jsonify({"is_recording": is_recording})

if __name__ == '__main__':
    app.run(debug=True)
