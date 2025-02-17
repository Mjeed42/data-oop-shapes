# pylint: disable=too-few-public-methods missing-module-docstring
import math


class Shape:
    """A base class representing a geometric shape with a color and name."""
    def __init__(self, color, name):
        self.name = name
        self.color = color

    def say_name(self):
        """Return a string introducing the shape by its name."""
        return f"My name is {self.name}."



class Rectangle(Shape):
    """A class representing a rectangle, inheriting from Shape."""
    def __init__(self, color, name, width, height):
        super().__init__(color, name)
        self.width = width
        self.height = height

    def say_name(self):
        """Return a string introducing the rectangle by its name."""
        return f"My name is {self.name} and I am a rectangle."

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


class Circle(Shape):
    """A class representing a circle, inheriting from Shape."""
    def __init__(self, color, name, radius):
        super().__init__(color, name)
        self.radius = radius

    def say_name(self):
        """Return a string introducing the circle by its name."""
        return f"My name is {self.name} and I am a circle."

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * self.radius * math.pi
