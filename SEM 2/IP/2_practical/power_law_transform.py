import cv2
import numpy as np
import matplotlib.pyplot as plt

# Open the image
img = cv2.imread('Img\\nuts.jpg')

# Convert the image to RGB (because OpenCV loads images in BGR format by default)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Initialize a figure for plotting
plt.figure(figsize=(10, 8))

# Try 4 gamma values
for idx, gamma in enumerate([0.2, 0.5, 1.0, 1.5, 2.0, 2.5]):
    # Apply gamma correction
    gamma_corrected = np.array(255*(img / 255) ** gamma, dtype='uint8')
    
    # Convert gamma-corrected image to RGB for correct display
    gamma_corrected_rgb = cv2.cvtColor(gamma_corrected, cv2.COLOR_BGR2RGB)
    
    # Plot the gamma-corrected image
    plt.subplot(2, 3, idx+1)  # Arrange in a 2x2 grid
    plt.imshow(gamma_corrected_rgb)
    plt.title(f'Gamma = {gamma}')
    plt.axis('off')  # Turn off axis for better viewing

# Display all the images in one plot
plt.tight_layout()
plt.show()
