from ArabicOcr import arabicocr
import cv2
import arabic_reshaper 
from bidi.algorithm import get_display
import numpy as np
from PIL import ImageFont, ImageDraw, Image

image_path="./images/ar_img.png"
img = cv2.imread(image_path)
fontpath = "arial.ttf" # <== download font
font = ImageFont.truetype(fontpath, 32)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)

results=arabicocr.arabic_ocr(image_path,image_path)

words =[]
l = 0
for i in range(len(results)):	
		word=results[i][1]
		reshaped_text = arabic_reshaper.reshape(word)
		bidi_text = get_display(reshaped_text)
		draw.text((50, 80 + l),bidi_text, font = font)
		l = l + 30
		words.append(word)

#pour ecrire le texte dans un fichier
with open ('file.txt','w',encoding='utf-8')as myfile:
		myfile.write(str(words))

img = np.array(img_pil)
cv2.imshow("arabic ocr image",img)
cv2.waitKey(0)
