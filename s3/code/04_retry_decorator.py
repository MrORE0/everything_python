"""
Live demo 4 -- A decorator with arguments: @retry(times=3)
Three layers: retry(...) -> decorator(func) -> wrapper(...)
"""

import time
from functools import wraps


def retry(times=3, delay=0.0):
    def decorator(func):
        # @wraps(func) copies the original function’s name and docstring onto the wrapper,
        # so flaky_request.__name__ stays 'flaky_request' instead of 'wrapper'
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    print(f"  attempt {attempt}/{times} failed: {exc}")
                    if attempt == times:
                        raise  # out of tries: let it fail loudly
                    time.sleep(delay)

        return wrapper

    return decorator


# NOTE: NOT the best way to do it, its for the sake of the example


# Functions are objects, so a function can hold data too:
# the call counter lives ON the function (flaky_request.calls).
# (flaky_request here is the decorated wrapper, so the attribute sits on that.)
@retry(times=3)
def flaky_request():
    flaky_request.calls += 1  # functions are objects, so they can hold data
    if flaky_request.calls < 3:  # fails twice, then works
        raise ConnectionError("server hiccup")
    return "200 OK"


flaky_request.calls = 0  # set it up after the function exists
print("result:", flaky_request(), "| calls:", flaky_request.calls)  # 200 OK | calls: 3


@retry(times=2)
def always_fails():
    raise ValueError("nope")


try:
    always_fails()
except ValueError as exc:
    print("gave up, error propagated:", exc)
