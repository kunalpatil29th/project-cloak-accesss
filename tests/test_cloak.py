

import unittest
import numpy as np
import cv2
import os
import sys

# Add the parent directory to sys.path to import from config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import settings

class TestCloakConfiguration(unittest.TestCase):
    """
    Unit tests for the project configuration.
    
    Definition: TestCase - The smallest unit of testing. It checks for a specific response to a 
    particular set of inputs.
    """
    
    def test_hsv_ranges(self):
        """
        Verify that HSV ranges are within valid OpenCV bounds (H: 0-180, S: 0-255, V: 0-255).
        """
        # Test Lower Red 1
        self.assertTrue(0 <= settings.LOWER_RED1[0] <= 180)
        self.assertTrue(0 <= settings.LOWER_RED1[1] <= 255)
        self.assertTrue(0 <= settings.LOWER_RED1[2] <= 255)
        
        # Test Upper Red 1
        self.assertTrue(0 <= settings.UPPER_RED1[0] <= 180)
        self.assertTrue(0 <= settings.UPPER_RED1[1] <= 255)
        self.assertTrue(0 <= settings.UPPER_RED1[2] <= 255)
        
        # Test Lower Red 2
        self.assertTrue(0 <= settings.LOWER_RED2[0] <= 180)
        self.assertTrue(0 <= settings.LOWER_RED2[1] <= 255)
        self.assertTrue(0 <= settings.LOWER_RED2[2] <= 255)
        
        # Test Upper Red 2
        self.assertTrue(0 <= settings.UPPER_RED2[0] <= 180)
        self.assertTrue(0 <= settings.UPPER_RED2[1] <= 255)
        self.assertTrue(0 <= settings.UPPER_RED2[2] <= 255)

    def test_hsv_order(self):
        """
        Verify that lower bounds are less than or equal to upper bounds for each HSV range.
        """
        # Test Red 1 range
        self.assertTrue((settings.LOWER_RED1 <= settings.UPPER_RED1).all())
        
        # Test Red 2 range
        self.assertTrue((settings.LOWER_RED2 <= settings.UPPER_RED2).all())

    def test_kernel_size(self):
        """
        Verify that the morphological kernel size is a tuple of positive integers.
        """
        self.assertIsInstance(settings.KERNEL_SIZE, tuple)
        self.assertEqual(len(settings.KERNEL_SIZE), 2)
        self.assertGreater(settings.KERNEL_SIZE[0], 0)
        self.assertGreater(settings.KERNEL_SIZE[1], 0)
        self.assertEqual(settings.KERNEL_SIZE[0], settings.KERNEL_SIZE[1])

    def test_dilation_iterations(self):
        """
        Verify that dilation iterations is a positive integer.
        """
        self.assertIsInstance(settings.DILATION_ITERATIONS, int)
        self.assertGreater(settings.DILATION_ITERATIONS, 0)

    def test_camera_settings(self):
        """
        Verify camera settings are valid.
        """
        self.assertIsInstance(settings.CAMERA_ID, int)
        self.assertGreaterEqual(settings.CAMERA_ID, 0)
        self.assertIsInstance(settings.INITIALIZATION_DELAY, (int, float))
        self.assertGreaterEqual(settings.INITIALIZATION_DELAY, 0)
        self.assertIsInstance(settings.BACKGROUND_CAPTURE_DELAY, (int, float))
        self.assertGreaterEqual(settings.BACKGROUND_CAPTURE_DELAY, 0)

    def test_video_settings(self):
        """
        Verify video export settings are valid.
        """
        self.assertIsInstance(settings.VIDEO_OUTPUT_PATH, str)
        self.assertGreater(len(settings.VIDEO_OUTPUT_PATH), 0)
        self.assertIsInstance(settings.VIDEO_CODEC, str)
        self.assertEqual(len(settings.VIDEO_CODEC), 4)
        self.assertIsInstance(settings.VIDEO_FPS, (int, float))
        self.assertGreater(settings.VIDEO_FPS, 0)

class TestColorUtils(unittest.TestCase):
    """
    Unit tests for color utility functions.
    """
    
    def test_numpy_array_types(self):
        """
        Verify that HSV settings are numpy arrays with correct dtype.
        """
        self.assertIsInstance(settings.LOWER_RED1, np.ndarray)
        self.assertEqual(settings.LOWER_RED1.dtype, np.int64)
        self.assertEqual(len(settings.LOWER_RED1), 3)

class TestConfigurationConstants(unittest.TestCase):
    """
    Unit tests for configuration constants.
    """
    
    def test_window_names(self):
        """
        Verify window names are non-empty strings.
        """
        self.assertIsInstance(settings.WINDOW_NAME, str)
        self.assertGreater(len(settings.WINDOW_NAME), 0)
        self.assertIsInstance(settings.TUNING_WINDOW_NAME, str)
        self.assertGreater(len(settings.TUNING_WINDOW_NAME), 0)

if __name__ == "__main__":
    unittest.main()
