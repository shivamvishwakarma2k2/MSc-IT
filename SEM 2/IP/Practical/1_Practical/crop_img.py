import cv2

img = cv2.imread("Img\\peacock.jpeg", 0)

height, width = img.shape[0:2]
startRow = int(height*.25)
startCol = int(width*.15)
endRow = int(height*.95)
endCol = int(width*.95)

croppedImage = img[startRow:endRow, startCol:endCol]

cv2.imshow("Original Image", img) 
cv2.imshow("Croped Image", croppedImage)
cv2.waitKey(0)