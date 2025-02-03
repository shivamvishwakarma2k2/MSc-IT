import cv2
import numpy as np
import matplotlib.pyplot as plt

def weighted_average_filter(image, weights):
    return cv2.filter2D(image, -1, weights / np.sum(weights))

img = cv2.imread('Img\\human.jpeg') # Reading the image

# Convert the image from BGR (OpenCV default) to RGB (for matplotlib display)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Define a simple weight mask (adjust as needed)
weight1 = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]])
weight2 = np.array([[1, 4, 1],
                   [4, 9, 4],
                   [1, 4, 1]])
# Apply the filter
filtered_image1 = weighted_average_filter(img, weight1)
filtered_image2 = weighted_average_filter(img, weight2)

plt.figure(figsize=(12, 5))  # Set figure size

plt.subplot(1, 3, 1)  
plt.imshow(img)
plt.title(f'Original Image')
plt.axis('off')

plt.subplot(1, 3, 2) 
plt.imshow(filtered_image1)
plt.title(f'Filtered Image 1')
plt.axis('off')

plt.subplot(1, 3, 3) 
plt.imshow(filtered_image2)
plt.title(f'Filtered Image 2')
plt.axis('off')

plt.tight_layout()  
plt.show()