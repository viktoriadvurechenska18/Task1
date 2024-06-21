import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class IDrawable(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape, IDrawable):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    
    def draw(self):
        print(f"Drawing a circle with radius {self.radius}")

class Square(Shape, IDrawable):
    def __init__(self, side_length):
        self.side_length = side_length
    
    def calculate_area(self):
        return self.side_length ** 2
    
    def draw(self):
        print(f"Drawing a square with side length {self.side_length}")


class Triangle(Shape, IDrawable):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return 0.5 * self.base * self.height
    
    def draw(self):
        print(f"Drawing a triangle with base {self.base} and height {self.height}")


def main():
    shapes = [
        Circle(5),
        Square(4),
        Triangle(3, 6)
    ]
    
    for shape in shapes:
        print(f"The area is {shape.calculate_area()}")
        shape.draw()

if __name__ == "__main__":
    main()