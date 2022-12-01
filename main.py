import cv2
from PIL import Image

image_path = "albin1.png"
cat_face_cascade = cv2.CascadeClassifier("haarcascade_frontalcatface_extended.xml")
image = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(image)
image = Image.open(image_path)
glasses = Image.open("glasses2.png")
glasses = glasses.convert("RGBA")
print(cat_face)
for (x, y, w, h) in cat_face:
    glasses = glasses.resize((w, int(h/3)))
    image.paste(glasses, (x, int(y+h/4)), glasses)
    image.save("image_new.png")
    image_new = cv2.imread("image_new.png")
    cv2.imshow("image_new", image_new)
    cv2.waitKey()