"""
Live demo 3 -- Generics, Callable and TypedDict
Check it:  mypy 03_generics_typeddict.py   (one deliberate error at the bottom)
"""

from typing import Callable, TypedDict

Stats = tuple[float, float, float]              # (min, mean, max): a named alias


def summarize(readings: list[float]) -> Stats:
    return min(readings), sum(readings) / len(readings), max(readings)


per_station: dict[str, Stats] = {               # the billion-row result, typed
    "Hamburg": summarize([8.9, 12.0, 10.1]),
}
print(per_station)


def apply_all(funcs: list[Callable[[float], float]], x: float) -> list[float]:
    return [f(x) for f in funcs]                # functions are objects (week 3)


print(apply_all([abs, lambda t: t * 2], -3.5))


class Reading(TypedDict):                       # the SHAPE of a dict (e.g. JSON)
    station: str
    temperature: float


record: Reading = {"station": "Oslo", "temperature": 5.7}
print(record["station"], record["temperature"])


def bad_example() -> None:
    print(record["temprature"])                 # mypy: TypedDict has no key "temprature"
