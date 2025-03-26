import cv2
import numpy as np

img = cv2.imread("Img\\harley.png")
contrasted_img = cv2.addWeighted(img, 2, np.zeros(img.shape, img.dtype), 0, 0)

cv2.imshow("Original", img)
cv2.imshow("contrasted_img", contrasted_img)

cv2.waitKey(0)
cv2.destroyAllWindows()