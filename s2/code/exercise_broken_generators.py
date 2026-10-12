"""
Week 2 exercise -- debug the broken generators.
"""

# --- A: the generator that only works once ---
squares = (n * n for n in range(5))
print("A total :", sum(squares))
print("A as list:", list(squares))


# --- B: indexing a generator ---
evens = (n for n in range(10) if n % 2 == 0)
try:
    print("B first even:", evens[0])
except Exception as e:
    print("B raised:", type(e).__name__, "-", e)


# --- C: the closed file ---
def read_lines(path):
    with open(path) as f:
        return (line.strip() for line in f)


try:
    lines = read_lines(__file__)
    print("C first line:", next(lines))
except Exception as e:
    print("C raised:", type(e).__name__, "-", e)


# --- D: the late-binding trap ---
gens = [(x * i for x in range(3)) for i in range(3)]
print("D:", [list(g) for g in gens])
