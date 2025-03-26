import cv2

# Load the images
img1 = cv2.imread('Img\\home_draw.png')  # First image
img2 = cv2.imread('Img\\sun_draw.png')   # Second image

# Resize the second image (img2) to match the size of the first image (img1)
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))  
 
# Blend the two images using weighted sum
# img1 gets 60% weight, img2 gets 40% weight, no scalar added
weightedSum = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)  

# Display the blended image
cv2.imshow('Weighted Image', weightedSum)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  