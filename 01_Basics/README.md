# 01_Basics - Simple Cloak

The simplest implementation of the invisibility cloak effect. Perfect for learning the core concepts!

## Concepts Covered

- **Video Capture**: Accessing and reading frames from a webcam
- **Color Space Conversion**: BGR → HSV for easier color detection
- **Image Masking**: Isolating specific color regions
- **Morphological Operations**: Removing noise from masks
- **Bitwise Operations**: Combining images using masks

## Usage

```bash
python simple_cloak.py
```

## How it Works

1. Captures a static background image
2. Continuously reads frames from the webcam
3. Converts each frame to HSV color space
4. Creates a mask for the red color range
5. Uses morphological operations to clean up the mask
6. Combines the background (where masked) with the original frame
