

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
