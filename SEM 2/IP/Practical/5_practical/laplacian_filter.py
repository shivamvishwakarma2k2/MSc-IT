import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Img\\charlie.jpg') # Read the image
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Convert to grayscale

# Apply Laplacian filter
laplacian = cv2.Laplacian(image, ddepth=cv2.CV_64F, ksize=3)  # CV_64F for better precision

# Convert back to uint8 for display
laplacian_uint8 = np.uint8(np.absolute(laplacian))

# **** Image Sharpening ****
# Create a kernel for sharpening
sharpening_kernel = np.array([[-1, -1, -1],
                              [-1,  9, -1],
                              [-1, -1, -1]])

# Apply the sharpening filter to the original image
sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)

# Display the images
plt.figure(figsize=(12, 8)) 
plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(laplacian_uint8)
plt.title("Laplacian Image")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(sharpened_image)
plt.title("Sharpened Image")
plt.axis('off')

plt.tight_layout()  # Adjust layout to avoid overlapping
plt.show()