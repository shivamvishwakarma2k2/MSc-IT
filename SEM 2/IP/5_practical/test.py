import cv2
import numpy as np
import matplotlib.pyplot as plt


# Read the image
image = cv2.imread("Img\\human.jpeg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert to double for calculations
gray = np.double(gray)

# Prewitt operator kernels
p_msk_x = np.array([[-1, 0, 1],
                     [-1, 0, 1],
                     [-1, 0, 1]])
p_msk_y = np.array([[-1, -1, -1],
                     [ 0,  0,  0],
                     [ 1,  1,  1]])

# Apply Prewitt operator along x and y axes
kx = cv2.filter2D(gray, -1, p_msk_x)
ky = cv2.filter2D(gray, -1, p_msk_y)

# Calculate edge magnitude
edge_magnitude = np.sqrt(kx ** 2 + ky ** 2)

# Display the images
# cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Original Image", 400, 400)
# cv2.imshow("Original Image", image)

# cv2.namedWindow("Edge Detection X", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Edge Detection X", 400, 400)
# cv2.imshow("Edge Detection X", np.abs(kx))

# cv2.namedWindow("Edge Detection Y", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Edge Detection Y", 400, 400)
# cv2.imshow("Edge Detection Y", np.abs(ky))

# cv2.namedWindow("Full Edge Detection", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Full Edge Detection", 400, 400)
# cv2.imshow("Full Edge Detection", np.abs(edge_magnitude))

# cv2.waitKey(0)
# cv2.destroyAllWindows()


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