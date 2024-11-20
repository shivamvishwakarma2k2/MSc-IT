import cv2

img = cv2.imread("Img\\harley.png")
 
# Resize with different interpolation methods
resized_image_linear = cv2.resize(img, (220, 150), interpolation=cv2.INTER_LINEAR)
resized_image_cubic = cv2.resize(img, (320, 180), interpolation=cv2.INTER_CUBIC)
resized_image_nearest = cv2.resize(img, (520, 240), interpolation=cv2.INTER_NEAREST)

print("original_image shape: ", img.shape)
print("resized_image_linear shape: ", resized_image_linear.shape)
print("resized_image_cubic shape: ", resized_image_cubic.shape)
print("resized_image_nearest shape: ", resized_image_nearest.shape)

cv2.imshow('original', img)
cv2.imshow('lin_Resize.jpg', resized_image_linear)
cv2.imshow('cub_resize.jpg', resized_image_cubic)
cv2.imshow('near_resize.jpg', resized_image_nearest)
cv2.waitKey(0)
cv2.destroyAllWindows()