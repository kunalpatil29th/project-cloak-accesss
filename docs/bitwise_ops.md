# Bitwise Operations in Computer Vision

In the **Project Cloak Access**, bitwise operations are the engines that perform the "magic" of invisibility. This document explains the core concepts used in our implementation.

## 🧱 Definitions

### 1. Bitwise Operations
The manipulation of individual bits within a binary representation of data. In image processing, these operations are performed pixel-by-pixel.

### 2. Bitwise AND
A logical operation that results in `1` (white/keep) only if both corresponding bits are `1`. 
- **Usage**: Used to extract specific regions of an image using a mask.
- **Example**: `cv2.bitwise_and(image, image, mask=mask)`

### 3. Bitwise NOT (Inversion)
A logical operation that flips all bits: `0` becomes `1`, and `1` becomes `0`.
- **Usage**: Used to create an inverse mask (e.g., to select everything *except* the cloak).
- **Example**: `cv2.bitwise_not(mask)`

### 4. Weighted Addition
The process of combining two images by assigning a weight (alpha/beta) to each.
- **Usage**: Used to blend the background and the foreground into a single seamless output.
- **Formula**: `output = image1 * alpha + image2 * beta + gamma`
- **Example**: `cv2.addWeighted(res1, 1, res2, 1, 0)`

---

## 🛠️ The Invisibility Workflow

1. **Mask Generation**: Identify the "cloak" pixels (Red color).
2. **Background Extraction**: Use **Bitwise AND** with the mask on the static background to keep only the background pixels where the cloak was.
3. **Foreground Extraction**: Use **Bitwise NOT** to invert the mask, then use **Bitwise AND** on the current frame to keep everything *except* the cloak.
4. **Final Blend**: Use **Weighted Addition** to merge the extracted background and the extracted foreground.
