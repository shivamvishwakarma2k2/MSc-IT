import cv2

img = cv2.imread("Img\\boat.jpg", 0)

# newImg = cv2.resize(img, (0,0), fx=0.75, fy=0.75) # 1st Way

newImg = cv2.resize(img, (220, 150))  # 2nd Way
print("Original shape: ", img.shape)
print("Resized shape: ", newImg.shape)

cv2.imshow('Original Image', img)
cv2.imshow('Resized Image', newImg)
cv2.waitKey(0)