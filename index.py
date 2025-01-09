from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import re

image = Image.open('image.jpg')

image = image.convert('L')

image = image.filter(ImageFilter.MedianFilter())

image = image.point(lambda x: 0 if x < 128 else 255)

enhancer = ImageEnhance.Contrast(image)
image = enhancer.enhance(2.0)

image.save('preprocessed_image.jpg')

config = '--psm 3' 
text = pytesseract.image_to_string(image, lang='kor+eng', config=config)

text = re.sub(r'\s+', ' ', text) 
text = text.strip()  # Remove leading/trailing whitespace

# Step 5: Save the extracted text to a file
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(text)

# Step 6: Print a success message
print("Text extracted and saved to 'output.txt'")
