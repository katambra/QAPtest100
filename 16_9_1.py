class Triangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


tr_1 = Triangle(4, 3, 40, 30)
print("Triangle (", tr_1.x,",", tr_1.y,",", tr_1.width,",", tr_1.height,")")