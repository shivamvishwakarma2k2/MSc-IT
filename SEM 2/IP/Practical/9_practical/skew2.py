import cv2
import numpy as np

def auto_correct_skew(image_path, scale_percent=50):
    # Read the image and Convert it to grayscale
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    gray = cv2.bitwise_not(gray) # Invert the grayscale image
    
    # Apply Otsu's thresholding to obtain a binary image
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Find the coordinates of non-zero pixels in the binary image
    coords = np.column_stack(np.where(thresh > 0))
    
    # Get the minimum bounding rectangle and its angle
    angle = cv2.minAreaRect(coords)[-1]

    # Correct the angle based on its orientation
    angle = -(90 + angle) if angle < -45 else -angle

    (h, w) = image.shape[:2] # Get the image dimensions
    
    # Calculate the center of the image
    center = (w // 2, h // 2)
    
    # Create a rotation matrix to rotate the image
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    
    # Apply the rotation to the image
    rotated_image = cv2.warpAffine(image, M, (w, h),
                                   flags=cv2.INTER_CUBIC,
                                   borderMode=cv2.BORDER_REPLICATE)
    
    # Resize images
    scale_percent = scale_percent  # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    image_resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    rotated_image_resized = cv2.resize(rotated_image, dim, interpolation=cv2.INTER_AREA)

    cv2.imshow('Original', image_resized)
    cv2.imshow('Auto-Corrected', rotated_image_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# driver
auto_correct_skew('Img\\skewed_text.png', scale_percent=70)