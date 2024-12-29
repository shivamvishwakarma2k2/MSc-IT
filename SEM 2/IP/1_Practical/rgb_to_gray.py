import cv2

img = cv2.imread("Img\\harley.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("RGB Image", img)
cv2.imshow("Grey Image", gray_img)
cv2.waitKeyEx(0)