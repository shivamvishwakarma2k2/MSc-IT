import cv2

# 0: grayscale, 1: Colored,  -1 = including alpha
img = cv2.imread("Img\\moon.jpg", -1) 
cv2.imshow("Image", img)
cv2.waitKey(1000)

print("type:", type(img))
print("shape", img.shape)