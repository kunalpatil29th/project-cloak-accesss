"""
Project Cloak Access: 03_Advanced - advanced_cloak.py

Definition:
Modular Programming: A software design technique that emphasizes separating the functionality of a 
program into independent, interchangeable modules, such that each contains everything necessary 
to execute only one aspect of the desired functionality.

Concepts:
1. Separation of Concerns: A design principle for separating a computer program into distinct 
   sections such that each section addresses a separate concern.
2. Refactoring: The process of restructuring existing computer code—changing the factorization—without 
   changing its external behavior.
"""

import cv2
import numpy as np
import time
import os
import sys

# Add the parent directory to sys.path to import from utils and config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.logger import logger
from config import settings

class InvisibleCloak:
    """
    Main class for the Invisibility Cloak project.
    
    Definition: Class - A code template for creating objects, providing initial values for state 
    and implementations of behavior.
    """
    def __init__(self):
        self.cap = cv2.VideoCapture(settings.CAMERA_ID)
        self.background = None
        self.video_writer = None
        logger.info("Initializing Invisible Cloak...")

    def _setup_video_writer(self, frame_size):
        """
        Initializes the VideoWriter object for exporting.
        
        Definition: VideoWriter - An OpenCV class for writing video files.
        """
        fourcc = cv2.VideoWriter_fourcc(*settings.VIDEO_CODEC)
        self.video_writer = cv2.VideoWriter(
            settings.VIDEO_OUTPUT_PATH,
            fourcc,
            settings.VIDEO_FPS,
            frame_size
        )
        logger.info(f"Video recorder initialized: {settings.VIDEO_OUTPUT_PATH}")

    def capture_background(self):
        """
        Captures the static background image.
        """
        logger.info(f"Please leave the frame. Capturing background in {settings.BACKGROUND_CAPTURE_DELAY} seconds...")
        time.sleep(settings.BACKGROUND_CAPTURE_DELAY)
        
        ret, frame = self.cap.read()
        if ret:
            self.background = np.flip(frame, axis=1)
            logger.info("Background captured successfully.")
        else:
            logger.error("Failed to capture background.")
            raise Exception("Camera capture failed.")

    def process_frame(self, frame):
        """
        Processes a single frame for the invisibility effect.
        """
        frame = np.flip(frame, axis=1)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create masks using settings
        mask1 = cv2.inRange(hsv, settings.LOWER_RED1, settings.UPPER_RED1)
        mask2 = cv2.inRange(hsv, settings.LOWER_RED2, settings.UPPER_RED2)
        mask = mask1 + mask2

        # Morphological operations
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones(settings.KERNEL_SIZE, np.uint8))
        mask = cv2.dilate(mask, np.ones(settings.KERNEL_SIZE, np.uint8), iterations=settings.DILATION_ITERATIONS)

        mask_inv = cv2.bitwise_not(mask)

        # Segment and combine
        res1 = cv2.bitwise_and(self.background, self.background, mask=mask)
        res2 = cv2.bitwise_and(frame, frame, mask=mask_inv)
        final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
        return final_output

    def run(self):
        """
        Main loop for processing video frames.
        """
        if self.background is None:
            self.capture_background()

        logger.info("Starting live processing. Press 'q' to quit.")
        
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                logger.warning("Lost camera feed.")
                break

            final_output = self.process_frame(frame)

            # Record if initialized
            if self.video_writer is None:
                self._setup_video_writer((final_output.shape[1], final_output.shape[0]))
            
            self.video_writer.write(final_output)

            cv2.imshow(settings.WINDOW_NAME, final_output)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                logger.info("User requested quit.")
                break

        self.cleanup()

    def cleanup(self):
        """
        Releases resources.
        """
        logger.info("Cleaning up resources...")
        if self.video_writer:
            self.video_writer.release()
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        cloak = InvisibleCloak()
        cloak.run()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
