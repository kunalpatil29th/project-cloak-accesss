# Web Interface for Invisible Cloak

This directory contains the Flask-based web interface for the Invisible Cloak project.

## Directory Structure
```
04_Web_Interface/
├── app.py                  # Main Flask application
├── README.md               # This file
├── requirements.txt        # Web interface dependencies
├── static/
│   ├── css/
│   │   └── style.css       # CSS styles
│   └── js/
│       └── main.js         # JavaScript interactions
└── templates/
    ├── history.html        # Session history template
    └── index.html          # Main page template
```

## Core Concepts

### 1. Flask Web Framework
Definition: Flask is a micro web framework for Python, meaning it provides only the essential tools and libraries needed to build a web application.
- Micro frameworks are lightweight and flexible, allowing developers to choose which tools and libraries to use.
- Flask provides routing, templating, and a development server out of the box.

### 2. Jinja2 Templates
Definition: Jinja2 is a templating engine for Python, used by Flask to dynamically generate HTML content.
- Templates allow you to separate the presentation logic from the application logic.
- You can use variables, loops, and conditionals in templates to dynamically generate content.

### 3. Database Manager
Definition: A class responsible for managing all database operations (creating tables, inserting records, querying data, etc.).
- The DatabaseManager in this project uses SQLite as the database engine.
- SQLite is a file-based database, meaning it doesn't require a separate database server.

### 4. Generator Function
Definition: A special type of function that returns an iterable set of items, one at a time, in a special way.
- Used for video streaming to efficiently deliver frames one at a time.
- Uses the `yield` keyword to return values without exiting the function.

### 5. AJAX
Definition: Asynchronous JavaScript and XML, a set of web development techniques that allows a web page to communicate with a server without reloading the page.
- Uses the Fetch API to make HTTP requests.
- Updates parts of the page dynamically without a full refresh.

## Key Features

### Live Video Stream
- Real-time video streaming from the camera
- Invisibility cloak effect applied to the stream
- Uses MJPEG streaming over HTTP

### Background Capture
- API endpoint to trigger background capture
- Client-side button to initiate capture
- Success/error feedback via alerts

### HSV Configuration Panel
- Interactive sliders for HSV range adjustment
- Real-time updates to the invisibility effect
- Two HSV ranges for better color detection (red has two ranges in HSV)

### Session History
- SQLite database to log all sessions
- Web page to display session history with timestamps
- Session duration calculation

## Installation and Usage

### 1. Install Dependencies
From the root of the project, install the web interface dependencies:
```bash
pip install -r 04_Web_Interface/requirements.txt
```

### 2. Run the Web Application
Navigate to the 04_Web_Interface directory and run:
```bash
cd 04_Web_Interface
python app.py
```

### 3. Access the Web Interface
Open your browser and go to: http://localhost:5000

## API Endpoints

### 1. GET /
- Returns the main page with the video stream.

### 2. GET /video_feed
- Returns the live video stream as MJPEG.

### 3. GET /capture_background
- Triggers background capture.
- Returns JSON: `{"status": "success", "message": "Background captured successfully!"}`

### 4. POST /update_hsv
- Updates the HSV color ranges.
- Request body: JSON with h1_low, s1_low, v1_low, h1_high, s1_high, v1_high, h2_low, s2_low, v2_low, h2_high, s2_high, v2_high.
- Returns JSON: `{"status": "success", "message": "HSV ranges updated!"}`

### 5. POST /update_morph
- Updates morphological parameters (kernel size, dilation iterations).
- Request body: JSON with kernel_size, dilation_iterations.
- Returns JSON: `{"status": "success", "message": "Morphological parameters updated!"}`

### 6. GET /history
- Returns the session history page.

## Technologies Used

- **Flask**: Web framework
- **OpenCV**: Computer vision for the invisibility effect
- **SQLite**: Database for session logging
- **Jinja2**: Templating engine
- **Fetch API**: AJAX requests from client-side
