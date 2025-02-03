import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Img\\erosion_dilation_ex.png',0) #load image

# Convert the image from BGR (default CV) to RGB for proper display with matplotlib
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define the structuring element for the morphological operations (3x3 matrix of ones)
# This defines the shape of the kernel that will be used for erosion and dilation.
str_element = np.ones((3,3), np.uint8) # one way
# str_element = np.array([1, 1, 1])  # other way

# The number of iterations (10) specifies how many times operation will be applied.
img_erosion = cv2.erode(image, str_element, iterations=10)
img_dilation = cv2.dilate(image, str_element, iterations=10)

plt.subplot(3, 1, 1)
plt.title("Original Image")
plt.imshow(image)
plt.axis("off")

plt.subplot(3, 1, 2)
plt.title("Erosion Image")
plt.imshow(img_erosion)
plt.axis("off")

plt.subplot(3, 1, 3)
plt.title("Dilation Image")
plt.imshow(img_dilation)
plt.axis("off")

plt.show()