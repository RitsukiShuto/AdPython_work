# Created by RitsukiShuto on 2021/01/15.
# facechange.py
#
import sys
import cv2

if len(sys.argv) != 3:
    print("usage: python", sys.argv[0], "backimage faceimage")
    sys.exit()

bimg  = cv2.imread(sys.argv[1])
fimg  = cv2.imread(sys.argv[2])
fdata = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')
gray  = cv2.cvtColor(bimg, cv2.COLOR_BGR2GRAY)

faces = fdata.detectMultiScale(gray, 1.3, 5)

print(faces)

for(x, y, w, h) in faces:
    fimg = cv2.resize(fimg, (w, h))
    bimg[y: y + h, x: x + w] = fimg

cv2.imshow('img', bimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
#end
