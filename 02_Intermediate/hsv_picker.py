"""
Project Cloak Access: 02_Intermediate - hsv_picker.py

Definition:
Event Handling: The process of responding to user inputs (like mouse clicks or key presses) 
during the execution of a program.

Concepts:
1. Pixel: Short for "Picture Element," it is the smallest unit of a digital image that can 
   be displayed and represented on a screen.
2. Callback Function: A function passed as an argument to another function, intended to be 
   executed after some event has occurred (in this case, a mouse click).
3. HSV: A color model that is more intuitive for human-centric tasks (like identifying a 
   color regardless of lighting conditions).
"""

import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    """
    Callback function that triggers on mouse events.
    
    Definition: setMouseCallback - An OpenCV function that registers a callback function for mouse events.
    """
    if event == cv2.EVENT_LBUTTONDOWN:
        # Get the pixel value at the clicked location
        pixel = frame[y, x]
        
        # Convert the single pixel to HSV
        # Definition: cvtColor - Converts an image from one color space to another.
        hsv_pixel = cv2.cvtColor(np.uint8([[pixel]]), cv2.COLOR_BGR2HSV)[0][0]
        
        print(f"--- Color at ({x}, {y}) ---")
        print(f"BGR: {pixel}")
        print(f"HSV: {hsv_pixel}")
        print("---------------------------")

# Initialize webcam
cap = cv2.VideoCapture(0)

print("Starting HSV Color Picker...")
print("Click on any object in the window to get its HSV value.")
print("Press 'q' to quit.")

cv2.namedWindow("HSV Color Picker")
cv2.setMouseCallback("HSV Color Picker", click_event)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = np.flip(frame, axis=1)
    
    cv2.imshow("HSV Color Picker", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
