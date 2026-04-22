"""
Project Cloak Access: tests - test_cloak.py

Definition:
Unit Testing: A software testing method by which individual units of source code—sets of one or 
more computer program modules together with associated control data, usage procedures, and 
operating procedures—are tested to determine whether they are fit for use.

Concepts:
1. Assertions: A confident and forceful statement of fact or belief. In programming, it's a 
   statement that a predicate is always true at that point in code execution.
2. Mocking: A process used in unit testing where the behavior of complex objects is simulated 
   to isolate the unit being tested.
"""

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

    def test_kernel_size(self):
        """
        Verify that the morphological kernel size is a tuple of positive integers.
        """
        self.assertIsInstance(settings.KERNEL_SIZE, tuple)
        self.assertEqual(len(settings.KERNEL_SIZE), 2)
        self.assertGreater(settings.KERNEL_SIZE[0], 0)
        self.assertGreater(settings.KERNEL_SIZE[1], 0)

if __name__ == "__main__":
    unittest.main()
