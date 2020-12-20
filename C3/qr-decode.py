# Created by RitsukiShuto on 2020/12/20.
# qr-decode.py
#
import sys
import cv2

if len(sys.argv) != 2:
    print("usage: python " + sys.argv[0] + "QRcode_file")
    sys.exit()

img = cv2.imread(sys.argv[1])
qr = cv2.QRCodeDetector()
data, points, straight_qrcode = qr.detectAndDecode(img)

print("data: ", data)
#end
