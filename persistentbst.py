"""
Binary search tree implementation.

In a consistent tree:
    compare(parent, right(parent)) is True
    compare(parent, left(parent)) is True

"""
from node import (left, set_left,
                  right, set_right,
                  value, make_node)


def _key_func(a):
    return a


def _equals(a, b):
    """
    check values for equality
    """
    return a == b


def push(tree, val, key=_key_func):
    """
    Pushes a new element to binary search tree
    """
    if tree is None:
        return make_node(None, val, None)
    else:
        parent_val = value(tree)
        if key(parent_val) > key(val):
            #goto left
            return set_left(tree, push(left(tree), val))
        else:
            # goto right
            return set_right(tree, push(right(tree), val))


def pop(tree, value, key=_key_func):
    # TODO
    pass


def contains(tree, value, key=_key_func):
    if tree is None:
        return False
    elif key(value(tree)) == key(value):
        return True
    else:
        if key(value(tree)) > key(value):
            # go to left
            return contains(left(tree), value)
        else:
            # go to right
            return contains(left(tree), value)
