"""
Week 1 exercise -- fixed versions of exercise_broken_snippets.py.
Reveal after pairs have predicted + run the broken versions.
"""

# --- A: fixed mutable default argument ---
def add_item_fixed(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket


print("A fixed:", add_item_fixed("apple"))
print("A fixed:", add_item_fixed("banana"))


# --- B: fixed row-multiplication trap ---
matrix_fixed = [[0] * 3 for _ in range(3)]
matrix_fixed[0][0] = 1
print("B fixed:", matrix_fixed)


# --- C: fixed rebinding vs mutating ---
def clear_list_fixed(lst):
    lst.clear()


nums_fixed = [1, 2, 3]
clear_list_fixed(nums_fixed)
print("C fixed:", nums_fixed)


# --- D: fixed shallow copy on a dict ---
import copy

config_fixed = {"options": ["a", "b"]}
backup_fixed = copy.deepcopy(config_fixed)
backup_fixed["options"].append("c")
print("D fixed:", config_fixed["options"])
