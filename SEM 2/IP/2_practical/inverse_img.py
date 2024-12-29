import cv2
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('Img\\satellite.jpg')

# Convert BGR to RGB for correct display in matplotlib
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Invert the image using cv2.bitwise_not
neg_img = cv2.bitwise_not(img)

# Convert the negative image from BGR to RGB for correct display
neg_img = cv2.cvtColor(neg_img, cv2.COLOR_BGR2RGB)

# Create a larger figure window
plt.figure(figsize=(12, 8))

# Display the original image
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(img)  # Display the RGB version
plt.axis('off')

# Display the negative image
plt.subplot(1, 2, 2)
plt.title('Negative Image')
plt.imshow(neg_img)  # Display the RGB version of the negative
plt.axis('off')

# Adjust layout to remove extra white space
plt.tight_layout()

# Show the images
plt.show()
