"""
Live demo 4 -- Infinite sequences
A generator doesn't need an end. YOU decide how much to take.
"""

from itertools import count, islice, takewhile


def fibonacci():
    a, b = 0, 1
    while True:  # never ends -- and that's fine
        yield a
        a, b = b, a + b


# build-in for loop
print("first 10 Fibonacci:", list(islice(fibonacci(), 10)))
# build-in for loop and if condition
print("Fibonacci below 100:", list(takewhile(lambda x: x < 100, fibonacci())))

# build-in iterator for generating numbers
print("evens:", list(islice(count(0, 2), 5)))
print("decimals:", list(islice(count(0, 0.5), 5)))


# Pretend this is a sensor / log stream that never stops
import random

random.seed(1)


def sensor_readings():
    while True:
        yield round(random.gauss(20, 3), 1)


# like a while loop with a condition in it
first_alert = next(r for r in sensor_readings() if r > 26)
print("first reading above 26:", first_alert)

# DON'T do this: list(fibonacci())  -> runs forever, eats all memory
