# Created by RitsukiShuto on 2021/01/15.
# cameradetect.py
#
import cv2

fdata = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    if not ret:
        # 映像取得に失敗 
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = fdata.detectMultiScale(gray, 1.3, 5)

    for(x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

    cv2.imshow('PUSH ENTER KEY', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
#end