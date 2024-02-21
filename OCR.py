from PIL import Image
import pytesseract

# Path to your image
image_path = 'path_to_your_image.jpg'

# Open the image
image = Image.open(image_path)

# Use pytesseract to do OCR on the image
text = pytesseract.image_to_string(image)

print(text)
