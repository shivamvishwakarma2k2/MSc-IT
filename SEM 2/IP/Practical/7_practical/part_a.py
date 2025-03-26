import cv2
import numpy as np

image = cv2.imread("Img/dices.png", 0)

# Create the structuring element for erosion
stelement2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# Perform erosion
img_erosion = cv2.erode(image, stelement2, iterations=1)

# Calculate the boundary by subtracting the eroded image from the original image
boundary = image - img_erosion

# Resize the images to smaller sizes
image_resized = cv2.resize(image, (300, 300))
boundary_resized = cv2.resize(boundary, (300, 300))

# Stack images horizontally (side by side)
img_frame = np.hstack((image_resized, boundary_resized))

# Display all images in one window
cv2.imshow('Images', img_frame)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()