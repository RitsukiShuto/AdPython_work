# Created by RitsukiShuto on 2021/01/21.
# main.py
#
import order1931074

# 3つの整数を入力
num1 = int(input("1st number = "))
num2 = int(input("2nd number = "))
num3 = int(input("3rd number = "))

max = order1931074.Order(num1, num2, num3)
mid = order1931074.Order(num1, num2, num3)
min = order1931074.Order(num1, num2, num3)

print("(max, mid, min) = (", max.max3(), ", ", mid.mid3(), ", ", min.min3(), ")")