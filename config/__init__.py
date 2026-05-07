"""
Project Cloak Access: config package

Definition:
Package - A way of organizing related modules into a single directory hierarchy.
"""

from .settings import (
    CAMERA_ID,
    INITIALIZATION_DELAY,
    BACKGROUND_CAPTURE_DELAY,
    LOWER_RED1,
    UPPER_RED1,
    LOWER_RED2,
    UPPER_RED2,
    KERNEL_SIZE,
    DILATION_ITERATIONS,
    WINDOW_NAME,
    TUNING_WINDOW_NAME,
    VIDEO_OUTPUT_PATH,
    VIDEO_CODEC,
    VIDEO_FPS
)

__all__ = [
    "CAMERA_ID",
    "INITIALIZATION_DELAY",
    "BACKGROUND_CAPTURE_DELAY",
    "LOWER_RED1",
    "UPPER_RED1",
    "LOWER_RED2",
    "UPPER_RED2",
    "KERNEL_SIZE",
    "DILATION_ITERATIONS",
    "WINDOW_NAME",
    "TUNING_WINDOW_NAME",
    "VIDEO_OUTPUT_PATH",
    "VIDEO_CODEC",
    "VIDEO_FPS"
]
