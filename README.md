# OCR
## Python project implementing Optical Character Recognition (OCR) 

OCR Project for Text Recognition<br>
This Python project implements Optical Character Recognition (OCR) for Arabic text using the library ArabicOcr and for other languages like english and frensh using the library EasyOCR.

Dependencies<br>
The project requires the following Python libraries:

cv2: OpenCV for image processing.<br>
arabic_reshaper: For reshaping Arabic text.<br>
bidi.algorithm: For bidirectional algorithm implementation.<br>
numpy: For numerical operations on arrays.<br>
Pillow: For manipulating images.<br>
ArabicOcr: Library specifically designed for OCR in Arabic text.<br>
EasyOCR: A popular OCR library with support for many languages.<br>

Files<br>
This repository contains the following files:<br>

arabicOcr.py: Python script containing the code to perform OCR using ArabicOcr library.<br>
ocr_test.py: Python script containing the code to perform OCR using EasyOCR library.<br>
images: a folder containing sample images containing text in different languages for testing the OCR implementation.<br>
README.md: This file, describing the contents of the repository.<br>

Usage<br>
To use the OCR implementation, simply run the arabic_ocr.py or easy_ocr.py script with Python:

Result<br>
The OCR implementation will output the recognized text from the input image. This text can be used for further processing or analysis.
