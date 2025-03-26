import cv2
import matplotlib.pyplot as plt

image = cv2.imread('Img\\satellite.jpg') # Reading the image

# Convert the image from BGR (OpenCV default) to RGB (for matplotlib display)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Check if image is loaded properly
if image is None:
    print("Error: Image not found or unable to open")
    exit()

# List of different kernel sizes for blurring
kernel_sizes = [3, 5, 7, 9, 11, 13]

plt.figure(figsize=(12, 8))  # Set figure size
plt.title("Avergaing filters")
plt.axis('off')

# Loop over the kernel sizes and apply the blur for each
for idx, value in enumerate(kernel_sizes):
    blur_img = cv2.blur(image, (value, value))
    plt.subplot(2, 3, idx + 1)  # Use idx+1 because subplot index starts from 1
    plt.imshow(blur_img)
    plt.title(f'Kernel({value}, {value})')
    plt.axis('off')  # Turn off axis for better viewing

plt.tight_layout()  # Adjust layout to avoid overlapping
plt.show()
