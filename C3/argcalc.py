# Created by RitsukiShuto on 2020/12/15.
# argcalc.py
#
import sys

def calc(x, y):
    print('add = ', x + y)
    print('sub = ', x - y)
    print('mul = ', x * y)
    print('div = ', x / y)

a = int(sys.argv[1])
b = int(sys.argv[2])

if b == 0:
    print('error!')
else:
    calc(a,b)
#end
