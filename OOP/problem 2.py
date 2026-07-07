class Shape:
    def area(self):
        return 0
class Rectangle:
    def __init__(self , width , height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(50,90)
print(rect.area())