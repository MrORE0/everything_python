"""
Live demo 4 -- Protocol: duck typing, but checked
"If it has a speak() method, it counts as a Speaker" -- no inheritance needed.
Check it:  mypy 04_protocol.py   (one deliberate error at the bottom)
"""

from typing import Protocol


class Speaker(Protocol):
    def speak(self) -> str: ...


class Dog:                       # does NOT inherit from Speaker
    def speak(self) -> str:
        return "Woof"


class Robot:
    def speak(self) -> str:
        return "Beep"


class Rock:
    pass                         # no speak()


def announce(thing: Speaker) -> None:
    print(thing.speak())


announce(Dog())
announce(Robot())


def bad_example() -> None:
    announce(Rock())             # mypy: "Rock" is incompatible with "Speaker"
