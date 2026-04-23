"""
Project Cloak Access: 01_Basics - simple_cloak.py

Definition: fsjfsojosdg
"""

import cv2
import numpy as np
import time

# Initialize webcam
# Definition: VideoCapture - A class for capturing video from video files, image sequences, or cameras.
cap = cv2.VideoCapture(0)
time.sleep(2)  # Small delay to let camera initialize

# Capture background
# Definition: Background Subtraction - A technique for generating a foreground mask relative to a static background.
print("Please leave the frame... Background will be captured in 2 seconds")
time.sleep(2) # Reduced for testing/quick setup

ret, background = cap.read()
if not ret:
    print("Error: Could not capture background.")
    exit()

background = np.flip(background, axis=1)  # Mirror the background

# Start processing frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = np.flip(frame, axis=1)  # Mirror the frame

    # Convert BGR to HSV
    # Definition: BGR (Blue-Green-Red) - The default color format used by OpenCV.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define red color range for cloak
    # Note: Red exists at both ends of the Hue spectrum (0-10 and 170-180).
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # Create masks for red color
    # Definition: inRange - A function that checks if array elements lie between the elements of two other arrays.
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2

    # Refine mask
    # Definition: MorphologyEx - Performs advanced morphological transformations.
    # MORPH_OPEN removes small noise.
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    # Dilation increases the object area.
    mask = cv2.dilate(mask, np.ones((3,3), np.uint8), iterations=1)

    # Invert mask to get non-cloak parts
    mask_inv = cv2.bitwise_not(mask)

    # Segment the frame and background
    # Definition: bitwise_and - Computes bitwise conjunction of two arrays or an array and a mask.
    res1 = cv2.bitwise_and(background, background, mask=mask)
    res2 = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Combine both results
    # Definition: addWeighted - Calculates the weighted sum of two arrays.
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    # Show output
    cv2.imshow("Invisible Cloak", final_output)

    # Quit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
