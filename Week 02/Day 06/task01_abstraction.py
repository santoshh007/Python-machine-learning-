#Create a set of classes representing different shapes, emphasizing abstraction by using abstract methods.
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def display_info(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def display_info(self):
        print("Circle:")
        print("Radius:", self.radius)
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())
        print()

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display_info(self):
        print("Rectangle:")
        print("Length:", self.length)
        print("Width:", self.width)
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())
        print()

class Triangle(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return (math.sqrt(3) / 4) * self.side_length ** 2

    def perimeter(self):
        return 3 * self.side_length

    def display_info(self):
        print("Triangle:")
        print("Side Length:", self.side_length)
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())
        print()

# Demonstration
circle = Circle(radius=5)
circle.display_info()

rectangle = Rectangle(length=4, width=6)
rectangle.display_info()

triangle = Triangle(side_length=5)
triangle.display_info()
