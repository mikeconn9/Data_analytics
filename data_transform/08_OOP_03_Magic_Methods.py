'''
# One usage is to override some build-in operations, such as +, -, x, /. __add__ to override '+'
# Python also provides: 
lt for <, le for <=, eq for ==, ne for !=, gt for >, ge for >=
# Majic methods for making classes act like containers:
len for len()
getitem for indexing
setitem for assigning to indexed values
delitem for deleting indexed values
iter for iteration over objects (e.g., in for loops)
contains for in
# x[y] = z: Majic method call: x.__setitem__(y, z)

'''

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def __add__(self, other):
        return BankAccount(self.balance + other.balance)

a = BankAccount(1024)
b = BankAccount(42)

result = a + b
print(result.balance)
