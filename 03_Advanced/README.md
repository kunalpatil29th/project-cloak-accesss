dj
## Architecture

```
InvisibleCloak class
├── __init__()              # Initialize camera and settings
├── capture_background()    # Capture static background
├── process_frame()         # Process single frame
├── update_hsv_ranges()     # Dynamic HSV updates
├── update_morphological_params()
├── run()                   # Main processing loop
└── cleanup()               # Release resources
```

## Usage

```bash
python advanced_cloak.py
```

## Features

- Object-oriented design
- Dynamic parameter updates
- Structured logging
- Video recording support
- Proper resource cleanup
