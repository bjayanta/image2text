import pytesseract as tess
from PIL import Image

# for windows 
# tess.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = Image.open('image.jpg') # read image
data = tess.image_to_string(img) # convert image to text 

# check the text is empty or not 
if data != "":
    f = open("data.txt", "w+")
    f.write(data)
    f.close()

# start analize 

# set categories & keywords 
categories = {
    "noun": ["lorem", "ipsum", "dummy"],
    "preposition": ["but", "with", "only", "of", "for"]
}

# some variables
output = {}
densities = {}
result = {}

total = len(data.split())

for category in categories:
    list = categories[category]
    
    for word in list:
        count = data.lower().count(word.lower())
        output.setdefault(category, {})[word] = count
        densities.setdefault(category, {})[word] = (count * 100) / total

for category in densities:
    group = densities[category]
    count = 0

    for density in group.values():
        count += density

    result[category] = count / len(group)

print(f"Total words: {total}")

print("\nCount words: ")
print(output)

print("\nWord density in percentage(%): ")
print(densities)

print("\nCategory wise density in percentage(%): ")
print(result)


print(data)
