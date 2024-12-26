# count: Counts up infinitely from a value
# cycle: Infinitely iterates through an iterable (for instance a list or string)
# repeat: Repeats an object, either infinitely or a specific number of times
# other functions: accumulate, takewhile, chain. In a simular way to map and filter
# product, permutation(all possible orders): When you want to accomplish a task with all possible combinations of some items.

from itertools import accumulate, takewhile, product, permutations

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x<=6, nums)))

letters = ("A", "B", "C")
print(list(product(letters, range(2))))
print(list(permutations(letters)))
print(set(product(letters, range(2))))
print(set(permutations(letters)))
# results:
# [('A', 0), ('A', 1), ('B', 0), ('B', 1), ('C', 0), ('C', 1)]
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
# {('B', 1), ('A', 1), ('B', 0), ('C', 1), ('A', 0), ('C', 0)}
# {('A', 'C', 'B'), ('B', 'C', 'A'), ('C', 'B', 'A'), ('A', 'B', 'C'), ('B', 'A', 'C'), ('C', 'A', 'B')}

