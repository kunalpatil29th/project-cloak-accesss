"""
Project Cloak Access: 01_Basics - simple_cloak.py

Definition:
Computer Vision: An interdisciplinary scientific field that deals with how computers can gain
high-level understanding from digital images or videos. It seeks to understand and automate
tasks that the human visual system can do.

Concepts:
1. Color Space Conversion: Transforming an image from one color space (e.g., BGR) to another (e.g., HSV)
   for easier color-based segmentation.
2. Image Segmentation: Partitioning a digital image into multiple segments (sets of pixels, also known as
   image objects) to simplify or change the representation of an image into something more meaningful
   and easier to analyze.
3. Error Handling: The process of responding to and managing exceptions that occur during program execution.
"""

import cv2
import numpy as np
import time

def main():
    """
    Main function to run the simple invisibility cloak.
    
    Definition: Main Function - The entry point of a program that controls the execution flow.
    """
    cap = None
    try:
        # Initialize webcam
        print("Initializing camera...")
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            raise RuntimeError("Could not open webcam. Please check if it's connected and not in use by another application.")
        
        time.sleep(2)  # Small delay to let camera initialize

        # Capture background
        print("Please leave the frame... Background will be captured in 2 seconds")
        time.sleep(2) # Reduced for testing/quick setup

        ret, background = cap.read()
        if not ret:
            raise RuntimeError("Could not capture background. Please try again.")

        background = np.flip(background, axis=1)  # Mirror the background
        print("Background captured successfully! Starting invisibility effect...")
        print("Press 'q' to quit.")

        # Start processing frames
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Warning: Could not read frame from camera.")
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
                print("Quitting...")
                break

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Cleanup resources
        if cap is not None and cap.isOpened():
            cap.release()
        cv2.destroyAllWindows()
        print("Resources cleaned up. Goodbye!")

if __name__ == "__main__":
    main()
