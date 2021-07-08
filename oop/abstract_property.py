"""
Abstract property (abstract attribute) = atribut abstract
- se declara cu doi decoratori
    @property
    @abstractmethod
Un atribut abstract este un mecanism de a accesa o metoda abstracta ca atribut
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width**2

    @property
    def perimeter(self):    
        return 4 * self.width


s = Square(6)
print(f'Area: {s.area()}')
print(f'Perimetrul: {s.perimeter()}')
