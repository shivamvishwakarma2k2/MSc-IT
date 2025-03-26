import cv2
import numpy as np
import matplotlib.pyplot as plt

def thinning_custom(img):
    size = np.size(img) # Get the size of the image
    # Create an empty image to store the skeletonized (thinned) version
    skel = np.zeros(img.shape, np.uint8)
    
    # Define a structuring element (cross-shaped) for morphological operations
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    
    done = False # Set a flag to indicate when to stop the thinning process

    while not done:  # Loop until the thinning is complete
        eroded = cv2.erode(img, element) # Perform erosion on the image
        temp = cv2.dilate(eroded, element)  # Perform dilation on the eroded image
        
        # Subtract  dilated result from the original image to get the edges
        temp = cv2.subtract(img, temp)
        
        # Add the edges to the skeleton image (accumulate the thinned parts)
        skel = cv2.bitwise_or(skel, temp)
        
        # Update the image with the eroded version for next iteration
        img = eroded.copy()

        # Check if all pixels are zero (image is empty)
        zeros = size - cv2.countNonZero(img)
        
        # If all pixels are zero, stop the thinning process
        if zeros == size:
            done = True

    return skel

def thickening_custom(img):
    size = np.size(img)
    thick = np.zeros(img.shape, np.uint8)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    done = False

    while not done:
        # Inverse of thinning
        dilated = cv2.dilate(img, element)
        temp = cv2.erode(dilated, element)
        
        temp = cv2.subtract(dilated, temp)
        thick = cv2.bitwise_or(thick, temp)
        img = dilated.copy()
        ones = cv2.countNonZero(img)
        if ones == size:
            done = True
    return thick

img = cv2.imread("Img\\steal_life.jpg", 0)

# Binarize the image using Otsu's thresholding
binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Apply the thinning and thickening operation on the binary image
thinning = thinning_custom(binary)
thickening = thickening_custom(binary)

# ********** Plotting **********
plt.subplot(1, 3, 1)
plt.imshow(binary, cmap='gray')
plt.title("Binarized Image")
plt.axis('off')  

plt.subplot(1, 3, 2)
plt.imshow(thinning, cmap='gray')
plt.title("Thinning")
plt.axis('off')  

plt.subplot(1, 3, 3)
plt.imshow(thickening, cmap='gray')
plt.title("Thickening")
plt.axis('off') 

plt.show()