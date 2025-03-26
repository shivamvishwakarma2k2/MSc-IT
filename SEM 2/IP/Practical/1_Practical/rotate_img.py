import cv2

img = cv2.imread("Img\\sea.jpeg")

cv2.imshow("Image", img) 
cv2.waitKey(1000)

height, width = img.shape[0:2]
print("height: ", height, "width: ", width)
rotationMatrix = cv2.getRotationMatrix2D((width/2, height/2), 90, .8)
rotatedImage = cv2.warpAffine(img, rotationMatrix, (width, height))
cv2.imshow("Rotated Image", rotatedImage)
cv2.waitKey(0)