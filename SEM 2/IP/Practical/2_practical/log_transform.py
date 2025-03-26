import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading the image (1 for color, 0 for grayscale, or -1 for unchanged)
img = cv2.imread('Img\\nuts.jpg')

# Converting to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Applying the log transformation
# Convert to float32 before applying log to avoid overflow and precision issues
gray_img_float = np.float32(gray_img)

# Calculate the constant 'c' for normalization
c = 255 / np.log(1 + np.max(gray_img_float))
log_transformed = c * np.log(1 + gray_img_float)

# Convert the result to uint8 for display purposes (normalized to 0-255)
# Clip to ensure values stay in the range [0, 255]
log_transformed = np.uint8(np.clip(log_transformed, 0, 255))  

# Display the original and log-transformed images side by side
plt.figure(figsize=(12, 8))

plt.subplot(1, 2, 1)
plt.title("Gray Image")
plt.imshow(gray_img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Log Transformed Image")
plt.imshow(log_transformed, cmap='gray')
plt.axis('off')

plt.show()