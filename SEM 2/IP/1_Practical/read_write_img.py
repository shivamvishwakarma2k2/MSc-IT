import cv2

# Read an image from the file system
img = cv2.imread("Img\\nature.jpeg") # Provide your image path here

# Write the image to disk
cv2.imwrite('Img\\output_nature.jpg', img)  