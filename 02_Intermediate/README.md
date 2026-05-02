# 02_Intermediate - Cloak with Tuning

An interactive version with real-time parameter tuning using trackbars!

## Concepts Covered

- **Graphical User Interface (GUI)**: Creating windows and UI elements
- **Trackbars**: Interactive controls for adjusting parameters
- **Real-time Tuning**: Modifying HSV ranges while seeing results
- **Parameter Calibration**: Finding optimal values for your environment

## Files

- `cloak_with_tuning.py`: Main script with HSV trackbars
- `hsv_picker.py`: Color picker utility

## Usage

```bash
python cloak_with_tuning.py
```

## Trackbar Controls

- **L-H**: Lower Hue (0-180)
- **L-S**: Lower Saturation (0-255)
- **L-V**: Lower Value (0-255)
- **U-H**: Upper Hue (0-180)
- **U-S**: Upper Saturation (0-255)
- **U-V**: Upper Value (0-255)

## Tips

1. Start with default values (red cloak)
2. Adjust trackbars to isolate your cloak color
3. Observe the "Mask" window to see what's being detected
4. Fine-tune until the cloak area is solid white in the mask
