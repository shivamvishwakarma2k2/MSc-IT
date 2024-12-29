import cv2
import numpy as np

# Step 1: Load an image
img = cv2.imread('Img\\harley.png')

# Step 2: Convert image from BGR (OpenCV default) to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Step 3: Split the image into its R, G, B channels
r_channel, g_channel, b_channel = cv2.split(img_rgb)

zeros = np.zeros_like(b_channel)
merged_image = cv2.merge((zeros, b_channel, g_channel, r_channel))

cv2.imshow('Red Channel',r_channel)  # Display Red Channel
cv2.imshow('Green Channel',g_channel)  # Display Green Channel
cv2.imshow('Blue Channel',b_channel)  # Display Blue Channel

cv2.namedWindow('Merged Image (Red Green and Blue Channels)', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Merged Image (Red Green and Blue Channels)', 400, 400)
cv2.imshow('Merged Image (Red Green and Blue Channels)', merged_image)


cv2.waitKey(0)
cv2.destroyAllWindows()