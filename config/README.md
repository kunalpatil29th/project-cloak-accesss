# Config Module

Centralized configuration settings for the entire project.

## Settings

### Camera

- `CAMERA_ID`: Webcam device index (default: 0)
- `INITIALIZATION_DELAY`: Camera warm-up time (seconds)
- `BACKGROUND_CAPTURE_DELAY`: Time to wait before capturing background

### HSV Color Ranges

- `LOWER_RED1`, `UPPER_RED1`: First red range (0-10)
- `LOWER_RED2`, `UPPER_RED2`: Second red range (170-180)

### Morphological Operations

- `KERNEL_SIZE`: Size of morphological kernel (tuple)
- `DILATION_ITERATIONS`: Number of dilation passes

### Video Export

- `VIDEO_OUTPUT_PATH`: Output filename
- `VIDEO_CODEC`: FourCC codec (mp4v)
- `VIDEO_FPS`: Frames per second

### Windows

- `WINDOW_NAME`: Main display window title
- `TUNING_WINDOW_NAME`: Tuning window title

## Usage

```python
from config import settings

print(settings.CAMERA_ID)
print(settings.LOWER_RED1)
```
