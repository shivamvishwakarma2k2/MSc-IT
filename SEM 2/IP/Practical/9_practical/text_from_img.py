import pytesseract as tess
from PIL import Image

# Set the path to the Tesseract executable (tesseract.exe)
# Ensure that the path points to the correct location of tesseract.exe
tess.pytesseract.tesseract_cmd = "9_practical\\setup\\tesseract.exe"

# Open the image from the specified file path using PIL (Pillow)
img = Image.open('Img\\text.png')

# Use Tesseract OCR to extract text from the image
# This function processes the image and converts it into a string (text)
text = tess.image_to_string(img)

# Print the extracted text to the console
print(text)
