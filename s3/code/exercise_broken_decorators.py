"""
Week 3 exercise (part 1) -- debug the broken decorators.

Work in pairs. For each snippet: predict the output on paper FIRST,
then run it, then explain why. Errors are caught so everything runs.
Solutions are in exercise_solutions.py -- don't peek until you've predicted.
"""


# --- A: the decorator that eats the result ---
def loud(func):
    def wrapper(*args, **kwargs):
        print("calling", func.__name__)
        func(*args, **kwargs)

    return wrapper


@loud
def add(a, b):
    return a + b


print("A:", add(2, 3))


# --- B: who am I? ---
def noisy(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@noisy
def area(r):
    """Area of a circle."""
    return 3.14159 * r * r


print("B:", area.__name__, "-", area.__doc__)


# --- C: the missing parentheses ---
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat
def hi():
    print("hi")


try:
    hi()
except Exception as e:
    print("C raised:", type(e).__name__, "-", e)


# --- D: the counter that cannot count ---
def count_calls(func):
    calls = 0

    def wrapper(*args, **kwargs):
        calls += 1
        return func(*args, **kwargs)

    return wrapper


@count_calls
def ping():
    return "pong"


try:
    ping()
except Exception as e:
    print("D raised:", type(e).__name__, "-", e)
