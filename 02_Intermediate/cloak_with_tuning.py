"""
Project Cloak Access: 02_Intermediate - cloak_with_tuning.py

Definition:
Real-time Parameter Tuning: A methodology used in computer vision to interactively adjust algorithm 
parameters (like HSV thresholds) while observing the effect on the output stream.

Concepts:
1. Trackbars: Graphical UI elements that allow users to select a value from a range by sliding a knob.
2. Calibration: The process of fine-tuning system parameters to achieve optimal performance in 
   specific environmental conditions (lighting, color of the cloak, etc.).
3. Callbacks: Functions that are executed in response to specific events or user actions.
"""

import cv2
import numpy as np
import time

def nothing(x):
    """
    Callback function for trackbars.
    Definition: Callback Function - A function passed as an argument to another function, 
    intended to be executed after some event has occurred.
    """
    pass

# Initialize webcam
# Definition: VideoCapture - A class for capturing video from video files, image sequences, or cameras.
cap = cv2.VideoCapture(0)
time.sleep(2)

# Create a window for trackbars
# Definition: namedWindow - Creates a window that can be used as a placeholder for images and trackbars.
cv2.namedWindow("Tuning")
cv2.createTrackbar("L-H", "Tuning", 0, 180, nothing)
cv2.createTrackbar("L-S", "Tuning", 120, 255, nothing)
cv2.createTrackbar("L-V", "Tuning", 70, 255, nothing)
cv2.createTrackbar("U-H", "Tuning", 10, 180, nothing)
cv2.createTrackbar("U-S", "Tuning", 255, 255, nothing)
cv2.createTrackbar("U-V", "Tuning", 255, 255, nothing)

print("Capturing background...")
time.sleep(2)
ret, background = cap.read()
if ret:
    background = np.flip(background, axis=1)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = np.flip(frame, axis=1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Get current positions of trackbars
    # Definition: getTrackbarPos - Returns the current position of the specified trackbar.
    lh = cv2.getTrackbarPos("L-H", "Tuning")
    ls = cv2.getTrackbarPos("L-S", "Tuning")
    lv = cv2.getTrackbarPos("L-V", "Tuning")
    uh = cv2.getTrackbarPos("U-H", "Tuning")
    us = cv2.getTrackbarPos("U-S", "Tuning")
    uv = cv2.getTrackbarPos("U-V", "Tuning")
    
    lower_range = np.array([lh, ls, lv])
    upper_range = np.array([uh, us, uv])
    
    # Create mask based on trackbar values
    # Definition: inRange - A function that checks if array elements lie between the elements of two other arrays.
    mask = cv2.inRange(hsv, lower_range, upper_range)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    
    mask_inv = cv2.bitwise_not(mask)
    res1 = cv2.bitwise_and(background, background, mask=mask)
    res2 = cv2.bitwise_and(frame, frame, mask=mask_inv)
    
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    
    cv2.imshow("Invisible Cloak - Tuning Mode", final_output)
    cv2.imshow("Mask", mask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
