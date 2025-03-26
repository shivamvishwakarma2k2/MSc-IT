import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("Img\\satellite.jpg")

# Convert BGR to RGB for correct color display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Apply Gaussian blur
blur_image = cv2.medianBlur(img, 5)

# Convert the blurred image to RGB for correct color display
blur_image_rgb = cv2.cvtColor(blur_image, cv2.COLOR_BGR2RGB)

# Plot the images with tight layout and large figure size
plt.figure(figsize=(12, 8))  # Larger figure size

# Display original image
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img_rgb)
plt.axis('off')

# Display blurred image
plt.subplot(1, 2, 2)
plt.title("Blurred Image")
plt.imshow(blur_image_rgb)
plt.axis('off')

# Automatically adjust subplot params to fit the figure area
plt.tight_layout()

# Show the plot
plt.show()
