import cv2

# Read the input and watermark images
img = cv2.imread('Img\\satellite.jpg')
watermark = cv2.imread("Img\\watermark.png")

# Resize watermark to fit within the size of the input image
watermark = cv2.resize(watermark, (img.shape[1], img.shape[0]))

# Calculate position to place the watermark in the center
wm_x = (img.shape[1] - watermark.shape[1]) // 2
wm_y = (img.shape[0] - watermark.shape[0]) // 2

# Blend images using addWeighted
result = img.copy()
result[wm_y:wm_y+watermark.shape[0], wm_x:wm_x+watermark.shape[1]] = cv2.addWeighted(
    img[wm_y:wm_y+watermark.shape[0], wm_x:wm_x+watermark.shape[1]], 0.7,
    watermark, 0.3, 0
)

cv2.namedWindow('Watermarked Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Watermarked Image', img.shape[1], img.shape[0])
cv2.imshow('Watermarked Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()