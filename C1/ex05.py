# Created by RitsukiShuto on 2020/12/08.
# ex05.py
#
num1 = int(input("Input 1st number : "))
num2 = int(input("Input 2nd number : "))

print("num1 = ", num1)
print("num2 = ", num2)

buf = num1
num1 = num2
num2 = buf

print("num1 = ", num1)
print("num2 = ", num2)