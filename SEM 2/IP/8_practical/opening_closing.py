import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Img\\nature.jpeg", 0) # Load the image

# Binarize the image using Otsu's thresholding
binarized = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Define a 3x3 kernel for morphological operation
kernel = np.ones((3, 3), np.uint8)

# Apply opening morphological operation
opening = cv2.morphologyEx(binarized, cv2.MORPH_OPEN, kernel, iterations=1)
closing = cv2.morphologyEx(binarized, cv2.MORPH_CLOSE, kernel, iterations=1)

# ********* plotting *********

# Plot the images
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(opening, cmap='gray')
plt.title("Opened Image")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(closing, cmap='gray')
plt.title("Closed Image")
plt.axis("off")

plt.show()