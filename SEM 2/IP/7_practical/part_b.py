import cv2
import numpy as np

image = cv2.imread("Img/dices.png", 0)
image_resized = cv2.resize(image, (300, 300))

# Edge detection using Canny
edges = cv2.Canny(image_resized, 100, 200)

# Find contours using the original image
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a blank image to draw contours
contour_image = np.zeros_like(image_resized)

# Draw contours on the blank image
cv2.drawContours(contour_image, contours, -1, (255, 255, 255), 1)

# Stack images: Original, Edge Detection, and Contours
stacked_images = np.hstack((image_resized, edges, contour_image))

# Display all images in one window
cv2.imshow('Image Extraction Techniques', stacked_images)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()