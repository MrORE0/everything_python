"""
Live demo 1 -- Type hints are NOT enforced when the program runs.

Setup (once):  pip install mypy ruff        (needs Python 3.10+)
1. Run it:       python3 01_hints_not_enforced.py   -> works, no complaints
2. Check it:     mypy 01_hints_not_enforced.py      -> flags the double("21") line
"""


def double(x: int) -> int:
    return x * 2


print(double(21))
print(double("21"))            # Python does not care: prints 2121
print(double.__annotations__)  # the hints are just stored, never checked


# A quick tour of the syntax
name: str = "Hamburg"                    # variable annotation
temps: list[float] = [12.0, 8.9]         # a list of floats
counts: dict[str, int] = {"Hamburg": 3}  # keys are str, values are int


def greet(name: str, times: int = 1) -> str:   # parameters and return value
    return (f"Hello, {name}! " * times).strip()


print(greet("Mert", 2))
