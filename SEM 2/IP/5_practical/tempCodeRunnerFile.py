import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("Img\\charlie.jpg", cv2.IMREAD_GRAYSCALE)

# Apply Sobel filter to get the horizontal edges (dx = 1, dy = 0)
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)

# Apply Sobel filter to get the vertical edges (dx = 0, dy = 1)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Compute the magnitude of the gradient (edge strength)
sobel_magnitude = cv2.magnitude(sobel_x, sobel_y)

# Convert the result back to uint8 for display
sobel_magnitude_uint8 = np.uint8(np.absolute(sobel_magnitude))

# Normalize the Sobel magnitude to match the original image intensity range (0 to 255)
sobel_magnitude_normalized = cv2.normalize(sobel_magnitude_uint8, None, 0, 255, cv2.NORM_MINMAX)

# Merge Sobel edges on top of the original image
combined_image = cv2.addWeighted(image, 0.7, sobel_magnitude_uint8, 0.3, 0)

# Display the Images
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(sobel_magnitude_normalized, cmap='gray')
plt.title('Sobel Edge Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(combined_image, cmap='gray')
plt.title('Original + Sobel Edges')
plt.axis('off')

plt.show()