import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("Img\\human.jpeg") 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert to double for calculations
gray = np.double(gray)

# Prewitt operator kernels
p_msk_x = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
    ])
p_msk_y = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
    ])

# Apply Prewitt operator along x and y axes
kx = cv2.filter2D(gray, -1, p_msk_x)
ky = cv2.filter2D(gray, -1, p_msk_y)

# Calculate edge magnitude
edge_magnitude = np.sqrt(kx ** 2 + ky ** 2)

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(np.abs(kx), cmap='gray')
plt.title('Edge Detection X')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(np.abs(ky), cmap='gray')
plt.title('Edge Detection Y')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(edge_magnitude, cmap='gray')
plt.title('Full Edge Detection')
plt.axis('off')

plt.show()