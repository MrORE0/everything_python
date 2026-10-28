"""
Live demo 5 -- A caching decorator, and a dynamic-programming problem
Question: how many ways to walk from the top-left to the bottom-right of an
N x N grid if you can only move right or down?
"""

import time
from functools import cache, wraps


def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"  {func.__name__}: {time.perf_counter() - start:.3f}s")
        return result

    return wrapper


# NOTE: how @cache essentially works
def my_cache(func):
    memo = {}  # closure memory

    @wraps(func)
    def wrapper(*args):
        if args not in memo:
            memo[args] = func(*args)  # compute once...
        return memo[args]  # remember forever

    return wrapper


def paths_slow(r, c):
    if r == 0 or c == 0:
        return 1
    return paths_slow(r - 1, c) + paths_slow(r, c - 1)


@my_cache
def paths_cached(r, c):
    if r == 0 or c == 0:
        return 1
    return paths_cached(r - 1, c) + paths_cached(r, c - 1)


@cache  # the standard-library version
def paths_stdlib(r, c):
    if r == 0 or c == 0:
        return 1
    return paths_stdlib(r - 1, c) + paths_stdlib(r, c - 1)


N = 12
print(f"grid {N}x{N}")
print("answer (no cache):", timed(paths_slow)(N, N))
print("answer (my_cache):", timed(paths_cached)(N, N))
print("answer (@cache)  :", timed(paths_stdlib)(N, N))

print("\nbig grid, only possible with a cache:")
big = timed(paths_stdlib)(100, 100)
print(
    f"100x100 grid: {len(str(big))}-digit answer"
)  # no-cache version would never finish
