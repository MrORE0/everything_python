"""
Live demo 5 -- Shallow vs deep copy
copy.copy() only copies the outer container; nested objects are shared.
"""

import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

shallow[0].append(99)

print("original:", original)
print("deep:", deep)
