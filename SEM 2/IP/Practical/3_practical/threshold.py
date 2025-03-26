import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Img\\satellite.jpg") 
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY) 
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV) 
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC) 
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO) 
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV) 

plt.figure(figsize=(12, 8)) 

plt.subplot(3, 2, 1) 
plt.imshow(thresh1) 
plt.title('Binary Threshold') 
plt.axis('off') 

plt.subplot(3, 2, 2) 
plt.imshow(thresh2) 
plt.title('Binary Threshold Inverted') 
plt.axis('off') 

plt.subplot(3, 2, 3)
plt.imshow(thresh3) 
plt.title('Truncated Threshold') 
plt.axis('off') 

plt.subplot(3, 2, 5) 
plt.imshow(thresh4) 
plt.title('Set to 0') 
plt.axis('off') 

plt.subplot(3, 2, 6)
plt.imshow(thresh5) 
plt.title('Set to 0 Inverted') 
plt.axis('off') 

plt.tight_layout()
plt.show()