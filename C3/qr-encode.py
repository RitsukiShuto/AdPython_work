# Created by RitsukiShuto on 2020/12/15.
# qr-encode.py
#
import sys
import qrcode

if len(sys.argv) != 3:
    print("usage: python " + sys.argv[0] + "code imagefile")
    sys.exit()

img = qrcode.make(sys.argv[1])
img.save(sys.argv[2])
#end
