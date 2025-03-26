import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('Img\\harley.png')

# Convert the image from BGR (OpenCV default) to RGB (for matplotlib)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Split the image into Blue, Green, and Red channels
b, g, r = cv2.split(image)

# Create a zero array with the same shape as the Blue channel
zeros = np.zeros_like(b)

# Merge the channels in the order: (zeros, g, b) for a new image that has only Green and Blue
merged_image = cv2.merge((zeros, g, b))

# Create a figure to display the images
plt.figure(figsize=(12, 10))

# Display the Original Image
plt.subplot(2, 3, 1)
plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')

# Display the Red Channel
plt.subplot(2, 3, 2)
plt.imshow(r, cmap='Reds')
plt.title('Red Channel')
plt.axis('off')

# Display the Green Channel
plt.subplot(2, 3, 3)
plt.imshow(g, cmap='Greens')
plt.title('Green Channel')
plt.axis('off')

# Display the Blue Channel
plt.subplot(2, 3, 4)
plt.imshow(b, cmap='Blues')
plt.title('Blue Channel')
plt.axis('off')

# Display the Merged Image (Green and Blue channels)
plt.subplot(2, 3, 5)
plt.imshow(merged_image)
plt.title('Merged Image (Green and Blue)')
plt.axis('off')

plt.tight_layout()
plt.show()
    