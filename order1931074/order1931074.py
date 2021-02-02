# Created by RitsukiShuto on 2021/01/21.
# order1931074.py
#
class Order():
    def __init__(self, l, n, m):
        self.x = l
        self.y = n
        self.z = m
    
    # 最大値を返す
    def max3(self):
        if(self.x > self.y):
            if(self.x > self.z):
                return self.x
            else:
                return self.z
                
        elif(self.y > self.z):
            return self.y
        else:
            return self.z

    # 中間値を返す
    def mid3(self):
        if(self.x > self.y):
            if(self.x > self.z):
                return self.z
            else:
                return self.x
                
        elif(self.y > self.z):
            return self.z
        else:
            return self.y

    # 最小値を返す
    def min3(self):
        if(self.x < self.y):
            if(self.x < self.z):
                return self.x
            else:
                return self.z
                
        elif(self.y < self.z):
            return self.y
        else:
            return self.z

if __name__ == '__main__':

    # 3つの整数を入力
    num1 = int(input("1st number = "))
    num2 = int(input("2nd number = "))
    num3 = int(input("3rd number = "))

    max = Order(num1, num2, num3)
    mid = Order(num1, num2, num3)
    min = Order(num1, num2, num3)

    print("(max, mid, min) = (", max.max3(), ", ", mid.mid3(), ", ", min.min3(), ")")
#end