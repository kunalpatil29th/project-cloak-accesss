# 04_Web_Interface - Flask Web Application

A web-based interface for the invisibility cloak effect using Flask!

## Concepts Covered

- **Web Framework**: Flask micro web framework
- **Routing**: URL to view function mapping
- **Video Streaming**: Multipart/x-mixed-replace streaming
- **AJAX**: Asynchronous JavaScript and XML requests
- **Templates**: Jinja2 templating engine
- **WebSockets/REST APIs**: Communicating with backend

## Features

- Real-time video streaming from your webcam
- Background capture button
- HSV range sliders for color tuning
- Morphological parameter controls
- Video recording (start/stop/download)
- Session history page

## Usage

```bash
python app.py
```

Then open your browser and visit:
[http://localhost:5000/](http://localhost:5000/)

## File Structure

```
04_web_interface/
├── app.py                  # Flask application backend
├── README.md               # This file
├── templates/
│   ├── index.html          # Main page
│   └── history.html        # Session history page
└── static/
    ├── css/
    │   └── style.css       # Stylesheet
    └── js/
        └── main.js         # Frontend JavaScript
```
