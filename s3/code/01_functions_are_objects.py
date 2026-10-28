"""
Live demo 1 -- Functions are objects
A function name is just a label pointing at a function object.
"""


def shout(text):
    return text.upper() + "!"


loud = shout
print(loud("hi"), "| same object?:", loud is shout)
print(shout.__name__, type(shout))


# Higher-order function: takes a function as an argument
def apply_twice(func, value):
    return func(func(value))


print(apply_twice(shout, "hey"))

# Built-ins you already use are higher-order too
words = ["banana", "Apple", "kiwi"]
print(sorted(words, key=str.lower))  # pass the function, don't call it
print(sorted(words, key=len))
print(list(map(len, words)))
print(list(map(str.upper, words)))

# Functions in a dict: a "dispatch table", no if/elif chain needed
ops = {
    "upper": str.upper,
    "title": str.title,
    "reverse": lambda s: "".join(reversed(s)),  # we can also do `lambda s: s[::-1]``
}

for name, fn in ops.items():
    print(f"{name:<8}", fn("hello world"))
