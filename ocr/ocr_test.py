import cv2
import easyocr

img = cv2.imread("./images/ad_img.png")
#on peut changer la langue, on choisi anglais 'en' ou francais 'fr' ou autre
reader = easyocr.Reader(['en'], gpu =False)
result=reader.readtext(img, detail=1, paragraph=False)

#affichage du texte dans console
t =''
for res in result :
    t += res[1] + ' '
print(t)

for (bbox, text, prob) in result :
    #define boundries
    (tl, tr, br, bl)= bbox
    tl=(int(tl[0]), int(tl[1]))
    tr=(int(tr[0]), int(tr[1]))
    br=(int(br[0]), int(br[1]))
    bl=(int(bl[0]), int(bl[1]))

    text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
    #dessiner les rectangles qui encadre chaque caractère
    cv2.rectangle(img, tl, br,(255,212,161), 2)
    #ajouter les caractères sur chaque rectangle
    cv2.putText(img,text, (tl[0],tl[1]-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(220,77,42),2)

cv2.imshow('Image',img)
cv2.waitKey(0)
