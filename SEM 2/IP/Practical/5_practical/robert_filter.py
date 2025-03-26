import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image (grayscale)
image = cv2.imread("Img\\charlie.jpg", cv2.IMREAD_GRAYSCALE)

# Apply Roberts Cross filter (Horizontal and Vertical Gradient)
kernel_x = np.array([[1, 0], [0, -1]], dtype=np.float32)
kernel_y = np.array([[0, 1], [-1, 0]], dtype=np.float32)

# Convolve the image with both kernels to get the gradients
gradient_x = cv2.filter2D(image, -1, kernel_x)
gradient_y = cv2.filter2D(image, -1, kernel_y)

# Compute the gradient magnitude (edge strength)
magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

# Normalize the result to the range 0-255
magnitude = np.uint8(np.absolute(magnitude))

# Display the Original Image
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Display the Gradient in the X direction (Horizontal edges)
plt.subplot(2, 2, 2)
plt.imshow(gradient_x, cmap='gray')
plt.title('Roberts X Gradient (Horizontal Edges)')
plt.axis('off')

# Display the Gradient in the Y direction (Vertical edges)
plt.subplot(2, 2, 3)
plt.imshow(gradient_y, cmap='gray')
plt.title('Roberts Y Gradient (Vertical Edges)')
plt.axis('off')

# Display the Gradient Magnitude (Edges)
plt.subplot(2, 2, 4)
plt.imshow(magnitude, cmap='gray')
plt.title('Roberts Edge Magnitude')
plt.axis('off')

# Show the plot
plt.show()