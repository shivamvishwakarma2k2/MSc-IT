import cv2

img = cv2.imread("Img\\twins.jpg", 0) # 0: greyscale, 1: Colored,  -1 = including alpha

cv2.imshow("Image", img) 
cv2.waitKey(0)
new  = cv2.imread("Img\\twins_gray.jpg")
cv2.imshow("Image", new) 
cv2.waitKey(0)