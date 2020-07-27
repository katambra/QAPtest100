class Rectangle:
    def __init__(self, a, b):
        self.length = a
        self.width = b

    def get_area(self):
        return self.length*self.width


r1 = Rectangle(7, 9)
print(r1.get_area())