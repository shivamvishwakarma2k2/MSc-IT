import cv2
from matplotlib import pyplot as plt

# Read image in grayscale
img = cv2.imread('Img\\steal_life.jpg', 0)

# Histogram equalization on the grayscale image
equ = cv2.equalizeHist(img)

# List of images and their titles
images = [img, equ] 
titles = ['Original Image', 'Equalized Image']  
histograms = [img.ravel(), equ.ravel()]  

# Create a figure to display the images and histograms
plt.figure(figsize=(12, 8))

# Loop through the images and histograms for plotting
for i in range(2): 
    # Plot the image
    plt.subplot(2, 2, i * 2 + 1)  # Image subplot (odd positions 1 and 3)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
    
    # Plot the histogram
    plt.subplot(2, 2, i * 2 + 2)  # Histogram subplot (even positions 2 and 4)
    plt.hist(histograms[i], bins=256, range = [0, 256])
    plt.title(f'Histogram of {titles[i]}')

# Adjust layout and show the plots
plt.tight_layout()
plt.show()