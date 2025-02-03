import cv2
import matplotlib.pyplot as plt

# Load the image in grayscale (0 means grayscale)
image = cv2.imread("Img\\steal_life.jpg", 0)

# Create a 5x5 elliptical structuring element
stelement2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# Perform erosion on the image
img_erosion = cv2.erode(image, stelement2, iterations=1)

# Calculate the boundary by subtracting the eroded image from the original
boundary = image - img_erosion 

# ********** Plotting **********

# Plot the images using matplotlib.pyplot
plt.figure(figsize=(10, 8))

# Show the original image
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('off')

# Show the boundary image (difference between the original and eroded image)
plt.subplot(1, 2, 2)
plt.imshow(boundary, cmap='gray')
plt.title("Boundary Image")
plt.axis('off')

# Display the plots
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()