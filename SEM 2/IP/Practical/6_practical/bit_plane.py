import cv2
import numpy as np
import matplotlib.pyplot as plt

def bit_plane_slice(image, bit):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    bit_plane = np.bitwise_and(gray_image, 2**bit)
    bit_plane = (bit_plane * 255).astype(np.uint8)
    return bit_plane

image = cv2.imread('Img\\500note.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

for i in range(8):
    bit_plane = bit_plane_slice(image, i)
    plt.subplot(3, 3, i+1)
    plt.imshow(bit_plane, cmap='gray')
    plt.title(f'Bit Plane {i}')
    plt.axis('off')

plt.subplot(3, 3, 9)
plt.imshow(image, cmap='gray')
plt.title(f'Original Image')
plt.axis('off')
    
# Show all plots
plt.tight_layout()
plt.show()
