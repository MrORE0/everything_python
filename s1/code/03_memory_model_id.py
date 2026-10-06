"""
Live demo 3 -- id() and the memory model
Same value != same object. id() proves it.
"""

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("id(a) == id(b):", id(a) == id(b))  # True -- same object
print("id(a) == id(c):", id(a) == id(c))  # False -- equal value, different object
print("a is b:", a is b)
print("a == c:", a == c)
