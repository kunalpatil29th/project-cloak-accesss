"""
Project Cloak Access: 03_Advanced - advanced_cloak.py

Definition:
Object-Oriented Programming (OOP): A programming paradigm based on the concept of "objects", 
which can contain data (attributes) and code (methods). OOP promotes code reusability, 
modularity, and maintainability.

Concepts:
1. Encapsulation: Bundling data and methods that operate on the data within a single unit (class).
2. Abstraction: Hiding complex implementation details and exposing only necessary features.
3. Modularity: Dividing code into separate, reusable components.
4. Resource Management: Properly acquiring and releasing system resources (camera, files, etc.).
5. Type Hints: Annotations that indicate the expected type of variables, function parameters, and return values.
"""

import cv2
import numpy as np
import time
import os
import sys
from typing import Optional, Tuple

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
    def __init__(self) -> None:
        self.cap: cv2.VideoCapture = cv2.VideoCapture(settings.CAMERA_ID)
        self.background: Optional[np.ndarray] = None
        self.video_writer: Optional[cv2.VideoWriter] = None
        
        # Initialize HSV ranges from settings with dynamic update support
        self.lower_red1: np.ndarray = settings.LOWER_RED1
        self.upper_red1: np.ndarray = settings.UPPER_RED1
        self.lower_red2: np.ndarray = settings.LOWER_RED2
        self.upper_red2: np.ndarray = settings.UPPER_RED2
        self.kernel_size: Tuple[int, int] = settings.KERNEL_SIZE
        self.dilation_iterations: int = settings.DILATION_ITERATIONS
        
        logger.info("Initializing Invisible Cloak...")

    def _setup_video_writer(self, frame_size: Tuple[int, int]) -> None:
        """
        Initializes the VideoWriter object for exporting.
        
        Definition: VideoWriter - An OpenCV class for writing video files.
        """
        fourcc: int = cv2.VideoWriter_fourcc(*settings.VIDEO_CODEC)
        self.video_writer = cv2.VideoWriter(
            settings.VIDEO_OUTPUT_PATH,
            fourcc,
            settings.VIDEO_FPS,
            frame_size
        )
        logger.info(f"Video recorder initialized: {settings.VIDEO_OUTPUT_PATH}")

    def capture_background(self) -> None:
        """
        Captures the static background image.
        """
        logger.info(f"Please leave the frame. Capturing background in {settings.BACKGROUND_CAPTURE_DELAY} seconds...")
        time.sleep(settings.BACKGROUND_CAPTURE_DELAY)
        
        ret: bool
        frame: np.ndarray
        ret, frame = self.cap.read()
        if ret:
            self.background = np.flip(frame, axis=1)
            logger.info("Background captured successfully.")
        else:
            logger.error("Failed to capture background.")
            raise Exception("Camera capture failed.")

    def process_frame(self, frame: np.ndarray) -> np.ndarray:
        """
        Processes a single frame for the invisibility effect.
        """
        frame = np.flip(frame, axis=1)
        hsv: np.ndarray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create masks using dynamic instance variables
        mask1: np.ndarray = cv2.inRange(hsv, self.lower_red1, self.upper_red1)
        mask2: np.ndarray = cv2.inRange(hsv, self.lower_red2, self.upper_red2)
        mask: np.ndarray = mask1 + mask2

        # Morphological operations
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones(self.kernel_size, np.uint8))
        mask = cv2.dilate(mask, np.ones(self.kernel_size, np.uint8), iterations=self.dilation_iterations)

        mask_inv: np.ndarray = cv2.bitwise_not(mask)

        # Segment and combine
        res1: np.ndarray = cv2.bitwise_and(self.background, self.background, mask=mask)
        res2: np.ndarray = cv2.bitwise_and(frame, frame, mask=mask_inv)
        final_output: np.ndarray = cv2.addWeighted(res1, 1, res2, 1, 0)
        return final_output

    def update_hsv_ranges(self, lower1: np.ndarray, upper1: np.ndarray, lower2: np.ndarray, upper2: np.ndarray) -> None:
        """
        Updates the HSV color ranges dynamically.
        
        Definition: Setter Method - A method that updates the value of an instance variable, 
        often used to enforce data validation or trigger side effects.
        """
        self.lower_red1 = lower1
        self.upper_red1 = upper1
        self.lower_red2 = lower2
        self.upper_red2 = upper2
        logger.info("HSV ranges updated.")

    def update_morphological_params(self, kernel_size: Tuple[int, int], dilation_iterations: int) -> None:
        """
        Updates the morphological parameters dynamically.
        """
        self.kernel_size = kernel_size
        self.dilation_iterations = dilation_iterations
        logger.info("Morphological parameters updated.")

    def run(self) -> None:
        """
        Main loop for processing video frames.
        """
        if self.background is None:
            self.capture_background()

        logger.info("Starting live processing. Press 'q' to quit.")
        
        while self.cap.isOpened():
            ret: bool
            frame: np.ndarray
            ret, frame = self.cap.read()
            if not ret:
                logger.warning("Lost camera feed.")
                break

            final_output: np.ndarray = self.process_frame(frame)

            # Record if initialized
            if self.video_writer is None:
                self._setup_video_writer((final_output.shape[1], final_output.shape[0]))
            
            self.video_writer.write(final_output)

            cv2.imshow(settings.WINDOW_NAME, final_output)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                logger.info("User requested quit.")
                break

        self.cleanup()

    def cleanup(self) -> None:
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
        cloak: InvisibleCloak = InvisibleCloak()
        cloak.run()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
