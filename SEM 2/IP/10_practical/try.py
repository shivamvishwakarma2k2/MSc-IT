import cv2
import numpy as np

# Load input image as grayscale (single-channel)
gray_image = cv2.imread('Img\\text.jpg', cv2.IMREAD_GRAYSCALE)

# Convert to 3-channel format (required for GrabCut)
color_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

# Initialize mask and rectangle (adjust coordinates as needed)
mask = np.zeros(color_image.shape[:2], dtype=np.uint8)
rect = (50, 50, 450, 600)  # (x, y, width, height)

# Apply GrabCut algorithm
bgd_model = np.zeros((1, 65), np.float64)
fgd_model = np.zeros((1, 65), np.float64)
cv2.grabCut(color_image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

# Create final mask (0=background, 1=foreground)
binary_mask = np.where((mask == 0) | (mask == 2), 0, 1).astype("uint8")

# Apply mask to original grayscale/binary image
result = gray_image * binary_mask  # Works with single-channel images

# Save and display
cv2.imshow('Background Removed', result)
cv2.waitKey(0)
cv2.destroyAllWindows()