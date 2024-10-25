from math import pi

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
# Programa principal

circle = Circle(5)
print(circle.area())

rectangle = Rectangle(4, 6)
print(rectangle.area())