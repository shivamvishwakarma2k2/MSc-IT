import cv2 
  
# reading the images 
circle_img = cv2.imread('Img\\circle.png') 
star_img = cv2.imread('Img\\star.png') 
  
# subtract the images 
subtracted_img = cv2.subtract(star_img, circle_img) 
# EXPLANATION: 
# star_img is subtracted from circle_img,
# the pixel values of circle_img are subtracted 
# from the corresponding pixel values of star_img 

# TO show the output 
cv2.imshow('image', subtracted_img) 
cv2.waitKey(0) 
cv2.destroyAllWindows()