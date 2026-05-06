

import cv2
import numpy as np
import time
from typing import Optional

def nothing(x: int) -> None:
    """
    Callback function for trackbars.
    
    Definition: Callback Function - A function passed as an argument to another function, 
    intended to be executed after some event has occurred.
    """
    pass

def main() -> None:
    """
    Main function to run the tuning cloak.
    """
    cap: Optional[cv2.VideoCapture] = None
    try:
        # Initialize webcam
        print("Initializing camera...")
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            raise RuntimeError("Could not open webcam. Please check if it's connected and not in use by another application.")
        
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

        print("Please leave the frame... Background will be captured in 2 seconds")
        time.sleep(2)
        
        ret: bool
        background: np.ndarray
        ret, background = cap.read()
        if not ret:
            raise RuntimeError("Could not capture background. Please try again.")
        background = np.flip(background, axis=1)
        
        print("Background captured! Adjust trackbars to tune your cloak. Press 'q' to quit.")

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Warning: Could not read frame from camera.")
                break
            
            frame = np.flip(frame, axis=1)
            hsv: np.ndarray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
            # Get current positions of trackbars
            # Definition: getTrackbarPos - Returns the current position of the specified trackbar.
            lh: int = cv2.getTrackbarPos("L-H", "Tuning")
            ls: int = cv2.getTrackbarPos("L-S", "Tuning")
            lv: int = cv2.getTrackbarPos("L-V", "Tuning")
            uh: int = cv2.getTrackbarPos("U-H", "Tuning")
            us: int = cv2.getTrackbarPos("U-S", "Tuning")
            uv: int = cv2.getTrackbarPos("U-V", "Tuning")
            
            lower_range: np.ndarray = np.array([lh, ls, lv])
            upper_range: np.ndarray = np.array([uh, us, uv])
            
            # Create mask based on trackbar values
            # Definition: inRange - A function that checks if array elements lie between the elements of two other arrays.
            mask: np.ndarray = cv2.inRange(hsv, lower_range, upper_range)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
            
            mask_inv: np.ndarray = cv2.bitwise_not(mask)
            res1: np.ndarray = cv2.bitwise_and(background, background, mask=mask)
            res2: np.ndarray = cv2.bitwise_and(frame, frame, mask=mask_inv)
            
            final_output: np.ndarray = cv2.addWeighted(res1, 1, res2, 1, 0)
            
            cv2.imshow("Invisible Cloak - Tuning Mode", final_output)
            cv2.imshow("Mask", mask)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Quitting...")
                break

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cap is not None and cap.isOpened():
            cap.release()
        cv2.destroyAllWindows()
        print("Resources cleaned up. Goodbye!")

if __name__ == "__main__":
    main()
