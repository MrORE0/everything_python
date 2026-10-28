"""
Live demo 2 -- Closures
An inner function remembers the variables of the function that made it.
"""


def make_counter():
    count = 0

    def increment():
        nonlocal count  # we want to rebind the outer variable
        count += 1
        return count

    return increment


c1 = make_counter()
c2 = make_counter()
print(c1(), c1(), c1(), "| c2:", c2())  # 1 2 3 | c2: 1  (separate memory each)
print("peek inside:", c1.__closure__[0].cell_contents)


def make_multiplier(m):
    return lambda x: x * m


double, triple = make_multiplier(2), make_multiplier(3)
print(double(5), triple(5))


# ---------------------------------------------------------------------------
# Anatomy of a closure
#   1. A function is defined inside another function (a nested function)
#   2. The inner function references variables from the outer function
#   3. The outer function returns the inner function
# ---------------------------------------------------------------------------
def outer():
    message = "hello from outer"  # a variable of the OUTER function

    def inner():  # 1. nested function
        return message  # 2. uses the outer function's variable

    return inner  # 3. outer returns inner (not calling it!)


f = outer()  # outer() is finished...
print("\nanatomy:", f())  # ...but inner still remembers `message`


# The inner function keeps a REFERENCE to the variable, not a copy of its value
def reference_not_copy():
    x = 1

    def inner():
        return x

    x = 2  # changed AFTER inner was defined
    return inner


print("reference, not copy:", reference_not_copy()())  # 2, not 1
print("stored in __closure__:", f.__closure__[0].cell_contents)


# ---------------------------------------------------------------------------
# Common use cases
# ---------------------------------------------------------------------------


# 1. Function factories: functions that generate other functions
#    with pre-set behaviour
def make_greeter(greeting):
    def greeter(name):
        return f"{greeting}, {name}!"

    return greeter


hello = make_greeter("Hello")
howdy = make_greeter("Howdy")
print("\nfactory:", hello("Steve"), "|", howdy("Steve"))


# 2. Data hiding: protect a variable from being accessed directly
def make_account(balance):
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance

    def get_balance():
        return balance

    return deposit, get_balance  # `balance` itself is not exposed


deposit, get_balance = make_account(100)
deposit(50)
print("data hiding:", get_balance())  # 150
# There is no `account.balance` to overwrite by accident.
# NOTE: (Hidden, not secure: __closure__ can still be inspected. It prevents mistakes, not attackers.)


# 3. Event handling: remember state between user interactions
def make_click_handler(button_name):
    clicks = 0

    def on_click():
        nonlocal clicks
        clicks += 1
        print(f"  {button_name} clicked {clicks} time(s)")

    return on_click


# Each function with its own counter
handlers = {"save": make_click_handler("Save"), "cancel": make_click_handler("Cancel")}
print("\nevent handling:")
for event in ["save", "save", "cancel", "save"]:  # pretend these are user clicks
    handlers[event]()


# 4. Callbacks: functions passed around while keeping their context
def download(url, on_done):  # pretend this takes a while
    on_done(f"<html of {url}>")


def make_callback(job_id):
    def callback(result):
        print(f"  [{job_id}] finished with {result}")

    return callback


print("\ncallbacks:")
download("example.com", make_callback("job-1"))
download("python.org", make_callback("job-2"))
