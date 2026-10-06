"""
Live demo 1 -- References vs Copies
"""

a = [1, 2, 3]
b = a
b.append(4)

print("a:", a)
print("b is a:", b is a)
