from PIL import Image
import pytesseract

image = Image.open('241205_booster_pc_12.jpg')

text = pytesseract.image_to_string(image, lang='kor+eng')

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(text)

print("Text extracted and saved to 'output.txt'")