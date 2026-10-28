"""
Week 3 exercise (part 1) -- fixed versions of exercise_broken_decorators.py.
"""

from functools import wraps


# --- A: return the wrapped function's result ---
def loud(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("calling", func.__name__)
        return func(*args, **kwargs)  # <- was missing `return`

    return wrapper


@loud
def add(a, b):
    return a + b


print("A:", add(2, 3))


# --- B: @wraps keeps the original name and docstring ---
def noisy(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@noisy
def area(r):
    """Area of a circle."""
    return 3.14159 * r * r


print("B:", area.__name__, "-", area.__doc__)


# --- C: a decorator WITH arguments must be called: @repeat(3) ---
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)  # <- parentheses + argument
def hi():
    print("hi")


print("C:")
hi()


# --- D: nonlocal lets the inner function rebind the outer variable ---
def count_calls(func):
    calls = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal calls  # <- was missing
        calls += 1
        wrapper.calls = calls  # expose the count to callers
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


@count_calls
def ping():
    return "pong"


ping()
ping()
print("D: ping was called", ping.calls, "times")
