# Created by RitsukiShuto on 2021/01/15.
# camerachange.py
#
import sys
import cv2

fdata = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')
cam   = cv2.VideoCapture(0)
fimg  = cv2.imread(sys.argv[1])

while True:
    ret, frame = cam.read()

    if not ret:
        # 映像取得に失敗
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = fdata.detectMultScale(gray, 1.3, 5)

    for(x, y, w, h) in faces:
        resize_img = cv2.resize(fimg, (w, h))
        frame[y: y + h, x: x + w] = resize_img

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
#end