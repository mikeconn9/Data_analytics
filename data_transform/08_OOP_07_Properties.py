'''
Properties provide a way of customizing access to instance attributes. 
When the instance attribute with the same name as the method is accessed, the method will be called instead.
One common use of a property is to make an attribute read-only.
'''

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False
    
    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed
    
    @pineapple_allowed.setter
    def pineapple_allowed(self,value):
        if value:
            password = input("Enter the password:")
            if password == "Sw0":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert!")
    
pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)

class Number:
    def __init__(self, num):
        self.value = num
    
    @property
    def isEven(self):
        if self.value%2 == 0:
            return True
        else:
            return False

x = Number(int(input()))
print(x.isEven)