# Created by RitsukiShuto on 2020/12/20.
# image.py
#
import sys
import cv2

img = cv2.imread(sys.argv[1])
cv2.imshow(sys.argv[1], img)

cv2.waitKey(0)
cv2.destroyAllWindows()
#end