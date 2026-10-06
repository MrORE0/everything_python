"""
Live demo 2 -- Mutability
Mutable objects change in place. Immutable objects get replaced.
"""

x = [1, 2]
print("x:", x, "id:", id(x))
x.append(3)  # same object, new contents

s = "hi"
print("s:", s, "id:", id(s))
s += "!"  # new object, s just repoints

print("\nAFTER CHANGES:")
print("x:", x, "id:", id(x))
print("s:", s, "id:", id(s))
