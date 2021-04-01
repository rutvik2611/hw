class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

unittest = Square(88)
print(unittest.area())

unittest2 = Shape()
print((unittest2.area()))