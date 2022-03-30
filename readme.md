# Image to Text
Using Tesseract.

## Install Tesseract 

### Windows: 
01. Download [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki) & install. 

02. Add the executable file in your code. Like: 
```py 
tess.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
```


### Linux: 
Step 1: Update your system:
> sudo apt update

Step 2: Add Tesseract OCR 5 PPA to your system:
> sudo add-apt-repository ppa:alex-p/tesseract-ocr
or,
> sudo add-apt-repository ppa:alex-p/tesseract-ocr-devel

Step 3: Install Tesseract on Ubuntu:
> sudo apt install -y tesseract-ocr

Step 4: Confirm the Tesseract version installed.
> tesseract --version

## Install python package

> pip install pillow pytesseract

Thank you.

