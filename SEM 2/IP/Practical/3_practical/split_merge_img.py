import cv2
import numpy as np


image = cv2.imread('Img\\harley.png') # Load the image

# Split the image into Blue, Green, and Red channels
b, g, r = cv2.split(image)

# Create a zero array with the same shape as the Blue channel
zeros = np.zeros_like(b)

# Merge the channels in the order: (
# zeros, g, b) for a new image that has only the Green and Blue channels
merged_image = cv2.merge((zeros, r, g, b))

# Display the Original Image
cv2.imshow('Original Image', image)
cv2.imshow('Red Channel', r) # Display the Red Channel
cv2.imshow('Green Channel', g) # Display the Green Channel
cv2.imshow('Blue Channel', b) # Display the Blue Channel
cv2.imshow('Merged Image', merged_image) # Display the Merged Image
cv2.waitKey(0)
cv2.destroyAllWindows()