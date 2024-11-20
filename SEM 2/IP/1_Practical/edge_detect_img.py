import cv2

img = cv2.imread("Img\\moon.jpg")
edge_img = cv2.Canny(img,100,200)

cv2.imshow("Original", img)
cv2.imshow("edge_img", edge_img)

cv2.waitKey(0)
cv2.destroyAllWindows()