"""
Live demo 3 -- Your first decorator
A decorator is a function that takes a function and returns a function.
"""

import time
from functools import wraps  # before and after function


def timed(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)  # call the real function
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.3f}s")
        return result  # must return the function we are adjusting

    return wrapper


def slow_add(a, b):
    time.sleep(0.2)
    return a + b


# What the @ syntax really does:
slow_add = timed(slow_add)
print(slow_add(1, 2))


@timed  # same thing, one line
def slow_mul(a, b):
    time.sleep(0.1)
    return a * b


print(slow_mul(3, 4))  # changed forever (above)


# the wrapper replaces the original's identity
@timed
def documented():
    """I am documented."""


print("\nwithout @wraps:", documented.__name__, "-", documented.__doc__)


def timed_v2(func):
    @wraps(func)  # copies name, docstring, etc.
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.3f}s")
        return result

    return wrapper


@timed_v2
def documented_v2():
    """I am documented."""


print("with @wraps   :", documented_v2.__name__, "-", documented_v2.__doc__)
