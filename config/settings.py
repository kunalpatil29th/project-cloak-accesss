"""
Project Cloak Access: config - settings.py

Definition:
Configuration Management: The process of maintaining software settings in a centralized location 
to ensure consistency and ease of modification across different modules.

Concepts:
1. Constants: Fixed values that do not change during the execution of a program.
2. HSV Ranges: Predetermined color thresholds used for isolating specific objects in computer vision.
"""

import numpy as np

# Camera Settings
CAMERA_ID = 0
INITIALIZATION_DELAY = 2
BACKGROUND_CAPTURE_DELAY = 2

# HSV Color Ranges for Red Cloak
# Red spans across the hue 0-10 and 170-180 in OpenCV HSV format.
LOWER_RED1 = np.array([0, 120, 70])
UPPER_RED1 = np.array([10, 255, 255])
LOWER_RED2 = np.array([170, 120, 70])
UPPER_RED2 = np.array([180, 255, 255])

# Morphological Operation Settings
KERNEL_SIZE = (3, 3)
DILATION_ITERATIONS = 1

# Window Settings
WINDOW_NAME = "Invisible Cloak - Modular Version"
TUNING_WINDOW_NAME = "Tuning"
