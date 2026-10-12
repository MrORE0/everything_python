"""
Live demo 2 -- Generator functions and yield
"""


def count_up_to(n):
    print("  [start]")
    i = 1
    while i <= n:
        print(f"  [about to yield {i}]")
        yield i
        print(f"  [resumed after {i}]")
        i += 1
    print("  [done]")


gen = count_up_to(3)
print("created generator:", type(gen).__name__)
print("(nothing has run yet -- calling it only built the generator)\n")

print("next ->", next(gen))
print("pause at yield")
print("next ->", next(gen))
print("next ->", next(gen))
try:
    next(gen)
except StopIteration:
    print("StopIteration: the function body finished")


def countdown(start):
    while start > 0:
        yield start
        start -= 1


print("\n--- countdown ---")
# pumping out the whole generator at once
print(list(countdown(3)))


# yield from: delegate to another iterable
def flatten(list_of_lists):
    for sub in list_of_lists:
        yield from sub


print("\n--- yield from ---")
print(list(flatten([[1, 2], [3], [4, 5]])))

# Items come out one at a time as they’re asked for,
# so the lists never get merged into one big list in memory

""" Long version:

def flatten(list_of_lists):
    for sub in list_of_lists:
        for item in sub:
            yield item
"""
