from abc import ABC, abstractmethod
from math import pi
# Abstract classes are used to define methods that must be implemented by any subclass. In Python, we use the abc (Abstract Base Class) module to create abstract classes. You can define abstract methods that have no implementation in the base class, forcing subclasses to provide their own implementations.

class Shape(ABC):
    @abstractmethod  # deve ser usado para transformar shape em uma classe abstrata junto com (ABC)
    def area(self):
        pass # sem implementacao na classe abstrata

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


shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f'The area is {shape.area()}')

# test = Shape() # nao funciona pq shape e uma classe abstrata