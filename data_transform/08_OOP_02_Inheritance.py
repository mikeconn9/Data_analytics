class Vehicle:
    def horn(self):
        print("Beep!")

class Car(Vehicle):
    def __init__(self, name, color):
        self.name = name
        self.color = color

obj = Car("BMW", "red")
obj.horn()

#super:
class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()