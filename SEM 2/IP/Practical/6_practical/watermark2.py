import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Img\\satellite.jpg')
watermark = cv2.imread("Img\\watermark.png")

watermark  = cv2.resize(watermark, (img.shape[1], img.shape[0]))
watermarked_img = cv2.addWeighted(img, 0.7, watermark, 0.3, 0)

cv2.imshow('Watermarked Image', watermarked_img)
cv2.waitKey(0)
