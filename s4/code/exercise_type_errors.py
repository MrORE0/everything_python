"""
Week 4 exercise -- find and fix the type errors.

Do NOT run this with python. Work in pairs:
  1. Read each snippet and predict which line mypy will complain about.
  2. Run:  mypy exercise_type_errors.py      and compare with your guess.
  3. Fix every error until mypy says "Success".
Solutions are in exercise_solutions.py -- don't peek until you've tried.
"""

from typing import TypedDict


# --- A: silent wrong answer ---
def total_price(price: float, quantity: int) -> float:
    return price * quantity


def snippet_a() -> None:
    print(total_price("9.99", 3))       # Python would print 9.999.999.99!


# --- B: the None that crashes ---
def find_age(ages: dict[str, int], name: str) -> int | None:
    return ages.get(name)


def snippet_b() -> None:
    age = find_age({"ann": 30}, "bob")
    print(age + 1)


# --- C: returning the wrong thing ---
def parse_temp(raw: str) -> float:
    if raw == "":
        return None
    return float(raw)


# --- D: the dictionary with the wrong shape ---
class Reading(TypedDict):
    station: str
    temperature: float


def snippet_d() -> None:
    r: Reading = {"station": "Oslo"}
    print(r["temp"])


if __name__ == "__main__":
    print("Run mypy on this file, not python.")
