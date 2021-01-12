# Created by RitsukiShuto on 2021/01/12.
# facedetect.py
#
import sys
import cv2

if len(sys.argv) != 2:
    print("usage: python", sys.argv[0], "imagefile")
    sys.exit()

img = cv2.imread(sys.argv[1])
fdata = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')   # BUG
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

faces = fdata.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 5)

cv2.imshow('face', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#end