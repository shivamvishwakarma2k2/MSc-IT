import cv2
import numpy as np

def correct_skew_simple(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply edge detection using Canny
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    
    # Use Hough Line Transform to detect lines in the image
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    
    if lines is not None:
        # Get the first line's angle
        rho, theta = lines[0][0]
        angle = np.degrees(theta) - 90  # Convert to degrees and correct for angle
        
        # Rotate the image to correct the skew
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        corrected_image = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC)
        
        # Display the original and corrected images
        cv2.imshow('Original Image', image)
        cv2.imshow('Corrected Image', corrected_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Replace with your image path
correct_skew_simple('Img\\skewed_text.png')
