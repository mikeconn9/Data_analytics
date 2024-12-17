# Difference between a class method and a static method:
# Class methods are passed the calling class, static methods aren't
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())

# Static methods can be called without creating an object of the class.
class Calculator:
    @staticmethod
    def add(n1, n2):
        return n1+n2

n1 = int(input())
n2 = int(input())

print(Calculator.add(n1, n2))