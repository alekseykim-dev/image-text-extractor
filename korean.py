from PIL import Image, ImageFilter
import pytesseract


def extract_korean_text(image_path, output_path):
    try:
        image = Image.open(image_path)
        
        image = image.convert('L') 
        image = image.filter(ImageFilter.SHARPEN)
      
       
        text = pytesseract.image_to_string(image, lang='kor')
        
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(text)
        
        print(f"Text extracted and saved to '{output_path}'")
    except Exception as e:
        print(f"Error processing the image: {e}")

input_image = 'meta_sample.png'
output_file = 'output.txt'

extract_korean_text(input_image, output_file)
