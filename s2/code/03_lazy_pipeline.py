"""
Live demo 3 -- Lazy pipelines
ONE item travels through every stage before the next item is even produced.
Nothing is stored.
"""


def numbers():
    for n in range(1, 7):
        print(f"produce {n}")
        yield n


def squares(source):
    for n in source:
        print(f"  square {n}")
        yield n * n


def only_even(source):
    for n in source:
        if n % 2 == 0:
            print(f"    keep {n}")
            yield n
        else:
            print(f"    drop {n}")


pipeline = only_even(squares(numbers()))
print("pipeline built, nothing has run yet\n")

for value in pipeline:
    print(f"      -> got {value}\n")
