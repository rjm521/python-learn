#!/usr/bin/python3

class Rectangle: # 父类
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def area(self):
        return self.h * self.w

    def perimeter(self):
        return 2 * (self.h + self.w)

class Square(Rectangle): # 子类继承父类
    def __init__(self, l):
        super(Square, self).__init__(l, l)
        self.l = l

myShape = Square(2)
print("myShape area:      [%s]" % myShape.area())
print("myShape perimeter: [%s]" % myShape.perimeter())

yourShape = Rectangle(2, 3)
print("yourShape area:     [%s]" % yourShape.area())
print("yourShape perimeter:[%s]" % yourShape.perimeter())