"""
Live demo 7 -- partial, map / filter / reduce, and comprehensions
"""

from functools import partial, reduce


def mult(m, num):
    return m * num


double = partial(mult, 2)  # pre-fill the first argument
print("double(5)      :", double(5))

f3 = partial(mult, m=2)  # pre-fill by keyword
print("f3(num=5)      :", f3(num=5))
try:
    f3(5)  # 5 goes to m, which is already set!
except TypeError as exc:
    print("f3(5) raises  :", exc)

binary_to_int = partial(int, base=2)  # a realistic use
print("binary_to_int  :", binary_to_int("1010"))

nums = [1, 2, 3, 4, 5, 6]
print("\nmap/filter/reduce")
print(list(map(lambda n: n * n, nums)))
print(list(filter(lambda n: n % 2 == 0, nums)))
print(reduce(lambda acc, n: acc + n, nums))

print("\nsame thing as comprehensions (usually clearer in Python)")
print([n * n for n in nums])
print([n for n in nums if n % 2 == 0])
print(sum(nums))  # reduce with + has a built-in
