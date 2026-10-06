"""
Live demo 4 -- is vs ==
Keep this one short: == for values, is only for None/singletons.

Note: a = 1000; b = 1000 written as two literals in the SAME file often
comes out `is` True anyway -- CPython's compiler folds identical literal
constants within one code object, which masks the point. Build one value
at runtime (int("1000")) to see the real behavior. Worth mentioning this
if a sharp student tries the naive version and gets a "wrong" answer --
it's a good meta-example of "the mental model still has edge cases."
"""

a = 1000
b = int("1000")  # constructed at runtime, not folded into the same constant
print("a is b (big ints):", a is b)  # False -- different objects

c = 100
d = int("100")
print("c is d (small ints, cached):", c is d)  # True -- small ints (-5 to 256) are cached
