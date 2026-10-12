"""
Week 2 exercise -- fixed versions of exercise_broken_generators.py.
"""


# --- A: generators are one-shot. Make a new one, or store a list ---
def make_squares():
    return (n * n for n in range(5))


print("A total :", sum(make_squares()))
print("A as list:", list(make_squares()))  # fresh generator each time


# --- B: generators can't be indexed. Use next(), or islice for position ---
from itertools import islice

evens = (n for n in range(10) if n % 2 == 0)
print("B first even:", next(evens))
print("B third even:", next(islice((n for n in range(10) if n % 2 == 0), 2, None)))


# --- C: the `with` block closed the file before anything was read ---
def read_lines(path):
    with open(path) as f:
        for line in f:  # make the function itself a generator
            yield line.strip()


lines = read_lines(__file__)
print("C first line:", next(lines))


# --- D: i is looked up lazily, after the loop finished (i == 2 everywhere) ---
def make_gen(i):
    return (x * i for x in range(3))  # i is bound at call time


gens = [make_gen(i) for i in range(3)]
print("D:", [list(g) for g in gens])
