"""
Live demo 1 -- Iterables vs iterators
"""

s = "hello"
nums = [1, 2, 3]  # an iterable: can produce an iterator

it = iter(nums)  # an iterator: produces one item at a time
s_it = iter(s)

# Two different iter type
print(type(s), type(s_it))
print(type(nums), type(it))

print(next(it), next(it), next(it))

# Can we go beyond?
try:
    next(it)
except StopIteration:
    print("StopIteration -> this is how a for loop knows to stop")

# What `for x in nums:` really does
print("--- for loop, unrolled ---")
it = iter(nums)  # reasigning the label `it` to another object
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    print(x)

# Iterators are one-shot. Iterables (lists) are not.
it = iter(nums)
print(list(it))
print(list(it))  # already used up
print(iter(it) is it)  # an iterator is its own iterator
print(iter(nums) is nums)  # a list hands out a fresh iterator each time


# Writing your own iterator by hand (the long way)
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


print("--- custom iterator ---")
print(list(Countdown(3)))  # [3, 2, 1]
