from PIL import Image
import pytesseract

for i in range(1, 16):  
    image_filename = f'{i}.png' 
    try:
        image = Image.open(image_filename)
        
        text = pytesseract.image_to_string(image, lang='kor+eng')
        
        output_filename = f'output_{i}.txt'
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(text)
        
        print(f"Text extracted and saved to '{output_filename}'")
    except Exception as e:
        print(f"Failed to process {image_filename}: {e}")
