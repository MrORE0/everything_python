"""
Live demo 5 -- itertools quick tour (mention, don't linger)
Every function here is lazy: it returns an iterator.
"""

import itertools as it

print("islice  :", list(it.islice("ABCDEFG", 2, 5)))  # slice any iterator
print("chain   :", list(it.chain([1, 2], [3], [4, 5])))  # glue iterables
print("cycle   :", list(it.islice(it.cycle("AB"), 5)))  # repeat forever
print("accum   :", list(it.accumulate([1, 2, 3, 4])))  # running total
print("pairwise:", list(it.pairwise([1, 4, 9, 16])))  # 3.10+
print("product :", list(it.product("AB", [1, 2])))  # nested loops
print("combos  :", list(it.combinations("ABC", 2)))

# groupby only groups ADJACENT items, so sort first
words = sorted(["apple", "avocado", "banana", "blueberry", "cherry"])
for letter, group in it.groupby(words, key=lambda w: w[0]):
    print("groupby :", letter, list(group))

# so we don't get error if we are on a older version (batched is 3.12+)
if hasattr(it, "batched"):
    print("batched :", list(it.batched(range(7), 3)))
