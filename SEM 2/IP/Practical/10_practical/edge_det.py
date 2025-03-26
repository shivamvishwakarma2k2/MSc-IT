import cv2
import matplotlib.pyplot as plt

def edge_detection(image_path, scale_percent=50):
    image = cv2.imread(image_path)
    
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    image_resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    
    gray_image = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian Blur to reduce noise
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    
    # Perform Canny edge detection
    edges = cv2.Canny(blurred_image, threshold1=100, threshold2=200)
    
    # Display the images using Matplotlib
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for Matplotlib
    plt.title('Original Image')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(edges, cmap='gray')  
    plt.title('Edge Detected')
    plt.axis('off')
    plt.tight_layout()
    plt.show()

edge_detection('Img/drawen.png', scale_percent=30)