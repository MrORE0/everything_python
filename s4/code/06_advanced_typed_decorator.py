"""
Optional extension -- typing the week 3 decorator.
A plain `def timed(func)` hides the real signature from mypy. ParamSpec and
TypeVar tell it "the wrapper takes the same arguments and returns the same type".
Check it:  mypy 06_advanced_typed_decorator.py
"""

import time
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")      # stands for "whatever arguments the function takes"
R = TypeVar("R")        # stands for "whatever the function returns"


def timed(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.3f}s")
        return result
    return wrapper


@timed
def add(a: int, b: int) -> int:
    return a + b


print(add(1, 2))
# add("1", 2)   # try uncommenting: mypy now catches the wrong argument type
