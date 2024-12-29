import cv2
import numpy as np

# Load the image (grayscale)
image = cv2.imread("Img\\charlie.jpg", cv2.IMREAD_GRAYSCALE)

# Apply Sobel filter to get the horizontal edges (dx = 1, dy = 0)
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)

# Apply Sobel filter to get the vertical edges (dx = 0, dy = 1)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Compute the magnitude of the gradient (edge strength)
sobel_magnitude = cv2.magnitude(sobel_x, sobel_y)

# Convert the result back to uint8 for display
sobel_magnitude_uint8 = np.uint8(np.absolute(sobel_magnitude))

# Display the original and Sobel result
cv2.imshow("Original Image", image)
cv2.imshow("Sobel Magnitude", sobel_magnitude_uint8)
cv2.waitKey(0)
cv2.destroyAllWindows()
