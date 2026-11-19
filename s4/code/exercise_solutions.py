"""
Week 4 exercise -- fixed version of exercise_type_errors.py.   mypy: Success.
"""

from typing import TypedDict


# --- A: pass a float, not a str ---
def total_price(price: float, quantity: int) -> float:
    return price * quantity


def snippet_a() -> None:
    print(total_price(9.99, 3))          # was "9.99"


# --- B: handle None before using the value ---
def find_age(ages: dict[str, int], name: str) -> int | None:
    return ages.get(name)


def snippet_b() -> None:
    age = find_age({"ann": 30}, "bob")
    if age is None:
        print("unknown person")
    else:
        print(age + 1)


# --- C: either allow None in the return type, or never return it ---
def parse_temp(raw: str) -> float | None:     # the type now tells the truth
    if raw == "":
        return None
    return float(raw)


# --- D: fill in every key, and use the right key name ---
class Reading(TypedDict):
    station: str
    temperature: float


def snippet_d() -> None:
    r: Reading = {"station": "Oslo", "temperature": 5.7}
    print(r["temperature"])


if __name__ == "__main__":
    snippet_a()
    snippet_b()
    snippet_d()
