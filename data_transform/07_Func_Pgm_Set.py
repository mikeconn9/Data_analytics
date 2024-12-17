# Characteristics:
# Has len(), IN
# Unordered, can't be indexed
# Can't contain duplicate elements
# Use Add instead of append
# "remove" a specific element, "pop" remove an arbitrary element

# Convert a list to a set:
word_set = set(["spam","eggs","sausage"])
print(word_set)

word_set.remove("eggs") 
print(word_set)

first = {1,2,3,4,5,6}
second = {4,5,6,7,8,9}

print(first|second)
print(first&second)
print(first-second)
print(second-first)
print(first^second)

#Results:
#{'eggs', 'sausage', 'spam'}
#{'sausage', 'spam'}
#{1, 2, 3, 4, 5, 6, 7, 8, 9}
#{4, 5, 6}
#{1, 2, 3}
#{8, 9, 7}
#{1, 2, 3, 7, 8, 9}