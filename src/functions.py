import cv2
import pytesseract
import re

def save_binary_file(byte_array):
    with open('../data/api_image.png', 'w+b') as image:
        image.write(byte_array)

def licence_nr_extractor(image):

    rgb_image = cv2.imread(image)

    return re.search(r'[A-Z9]{5}\d{6}[A-Z9]{2}\d[A-Z]{2}',
                     pytesseract.image_to_string(rgb_image)).group()
