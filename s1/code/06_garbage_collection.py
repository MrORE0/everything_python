"""
Live demo 6 -- Garbage collection, made visible
Pause after gc.collect() -- nothing prints until then. That pause is the point.
"""

import gc


class Node:
    def __init__(self, name):
        self.name = name
        self.other: Node

    def __del__(self):
        print(f"{self.name} collected")


a = Node("A")
b = Node("B")
a.other = b
b.other = a  # cycle: A -> B -> A

# TODO: add an iteraction like, hit enter to collect them and showcase how they are still there
del a, b  # refcount never hits 0 here, nothing prints yet
gc.collect()  # cycle detector sweeps them now -- watch the output appear
