from flask import Flask, render_app, Response
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Project Cloak Access Web Interface!"

if __name__ == '__main__':
    app.run(debug=True)
