# Created by RitsukiShuto on 2021/01/16.
# checker.py
#
import sys
import cv2
import numpy as np

if len(sys.argv) == 1:
    img = cv2.imread("./images/portrait.jpg")
elif len(sys.argv) == 2:
    img = cv2.imread(sys.argv[1])
else:
    print("usage: $python", sys.argv[0], "[imagefile]")
    sys.exit()

cv2.imshow("IMAGE", img)

if len(img.shape) == 3:
    h, w, d = img.shape[:3]
else:
    h, w = img.shape[:2]
    d = 1

cv2.waitKey(0)

blk_x = w // 8  # block number == 8 (horizontal)
blk_y = h // 8  # block number == 8 (vertical)


for i in range(blk_x):
    for j in range(blk_y):
        img[i, j] = [255, 255, 255]

cv2.imshow("IMAGE", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# end