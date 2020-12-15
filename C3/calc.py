# Created by RitsukiShuto on 2020/12/15.
# calc.py
#
def calc(x, y):
    print('add = ', x + y)
    print('sub = ', x - y)
    print('mul = ', x * y)
    print('div = ', x / y)

a = int(input('a = '))
b = int(input('b = '))

if b == 0:
    print('error!')
else:
    calc(a, b)
#end