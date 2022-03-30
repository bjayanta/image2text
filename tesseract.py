import pytesseract as tess
from PIL import Image

# for windows 
# tess.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = Image.open('image.png')
text = tess.image_to_string(img)

if text != "":
    f = open("data.txt", "w+")
    f.write(text)
    f.close()

print(text)
