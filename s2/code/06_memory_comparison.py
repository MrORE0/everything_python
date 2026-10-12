"""
Live demo 6 -- Why laziness matters: memory
Same sum, very different cost.
"""

import sys
import tracemalloc

N = 3_000_000


def measure(label, fn):
    tracemalloc.start()
    result = fn()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"{label:<28} result={result}  peak memory={peak / 1024 / 1024:8.1f} MB")


measure("list comprehension", lambda: sum([n * n for n in range(N)]))
measure("generator expression", lambda: sum(n * n for n in range(N)))

print()
print(
    "size of the list object     :",
    sys.getsizeof([n for n in range(N)]) // 1024 // 1024,
    "MB (just the pointers)",
)
print("size of the generator object:", sys.getsizeof(n for n in range(N)), "bytes")
print("-> the generator is a recipe, not the finished dish")
