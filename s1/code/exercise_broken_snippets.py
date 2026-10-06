"""
Week 1 exercise -- debug the broken snippets.

Work in pairs. For each snippet: predict the output on paper FIRST,
then run it, then figure out why you were wrong (if you were).
Solutions are in exercise_solutions.py -- don't peek until you've predicted.
"""


# --- A: mutable default argument
def add_item(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket


print("A:", add_item("apple"))
print("A:", add_item("banana"))


# --- B: the row-multiplication trap ---
matrix = [[0] * 3] * 3
matrix[0][0] = 1
print("B:", matrix)


# --- C: rebinding vs mutating ---
def clear_list(lst):
    lst = []


nums = [1, 2, 3]
clear_list(nums)
print("C:", nums)


# --- D: shallow copy on a dict ---
import copy

config = {"options": ["a", "b"]}
backup = copy.copy(config)
backup["options"].append("c")
print("D:", config["options"])
