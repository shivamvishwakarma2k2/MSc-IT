import cv2
import numpy as np

# Load the input image
image = cv2.imread('Img\star.png')

# Initialize a mask with the same dimensions as the image
mask = np.zeros(image.shape[:2], dtype=np.uint8)

# Define the rectangle enclosing the foreground object (x, y, width, height)
# Adjust these values based on your specific image
rect = (50, 50, 450, 600)

# Initialize background and foreground models (used internally by GrabCut)
background_model = np.zeros((1, 65), np.float64)
foreground_model = np.zeros((1, 65), np.float64)

# Apply GrabCut algorithm with the defined rectangle
cv2.grabCut(
    image, 
    mask, 
    rect,
    background_model,
    foreground_model,
    iterCount=5,
    mode=cv2.GC_INIT_WITH_RECT
)

# Create a binary mask where 0 (background) and 2 (probable background) are 0
# and 1 (foreground) and 3 (probable foreground) are 1
binary_mask = np.where((mask == 0) | (mask == 2), 0, 1).astype('uint8')

# Apply the binary mask to the original image to extract the foreground
result = image * binary_mask[:, :, np.newaxis]

# Save the result
cv2.imwrite('output.jpg', result)

# Optional: Display the result (requires GUI support)
cv2.imshow('Foreground', result)
cv2.waitKey(0)
cv2.destroyAllWindows()