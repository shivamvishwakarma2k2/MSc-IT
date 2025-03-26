import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create a sample binary image (0 and 1 values)
image = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 1, 1, 0, 0, 0, 1],
                  [0, 1, 1, 1, 1, 0, 0, 1],
                  [0, 1, 1, 1, 1, 0, 0, 0],
                  [0, 0, 1, 0, 1, 1, 1, 1],
                  [0, 1, 0, 0, 0, 0, 0, 1],
                  [0, 1, 0, 0, 1, 0, 1, 1],
                  [0, 1, 0, 0, 0, 0, 0, 1]], dtype=np.uint8)

# Define the kernel for the Hit-or-Miss operation
kernel = np.array([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]], dtype=np.int8)

# Perform the Hit-or-Miss operation
result = cv2.morphologyEx(image, cv2.MORPH_HITMISS, kernel)

# Plot the original image
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('off')  # Hide the axes

# Plot the Hit-or-Miss result
plt.subplot(1, 2, 2)
plt.imshow(result, cmap='gray')
plt.title("Hit-or-Miss Result")
plt.axis('off')  # Hide the axes

# Display the images
plt.tight_layout()  # Adjust layout for better visualization
plt.show()
