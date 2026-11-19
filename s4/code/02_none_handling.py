"""
Live demo 2 -- mypy and None
Python runs this file fine, because bad_example() is never called.
mypy still reads it and reports the bug:   mypy 02_none_handling.py
"""

STATIONS = {"Hamburg": 9.7, "Oslo": 5.7}


def mean_temp(station: str) -> float | None:    # "a float, or None"
    return STATIONS.get(station)                # .get returns None if missing


def bad_example() -> float:
    return mean_temp("Oslo") + 1                # mypy: the value could be None!


def good_example() -> float:
    temp = mean_temp("Oslo")
    if temp is None:                            # handle the None case explicitly
        return 0.0
    return temp + 1                             # here mypy knows temp is a float


print(good_example())
