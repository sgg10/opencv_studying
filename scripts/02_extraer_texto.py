import cv2
import pytesseract

# sudo apt install tesseract-ocr
# sudo apt install tesseract-ocr-spa
# sudo apt install imagemagick
# pip install pytesseract
# pip install opencv-python


imgText = cv2.imread("imagen_texto.png")
print(pytesseract.image_to_string(imgText, lang='spa'))