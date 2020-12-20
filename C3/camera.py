# Created by RitsukiShuto on 2020/12/20.
# camera.py
#
import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    if not ret:
        break

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('output.ping', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
#end
