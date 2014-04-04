"""
Binary search tree implementation.
"""
from node import (left, set_left,
                  right, set_right,
                  value, make_node,
                  count)


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


def contains(tree, val, key=_key_func):
    """
    Checks if tree contains given node.
    """
    if tree is None:
        return False
    elif key(value(tree)) == key(val):
        return True
    else:
        if key(value(tree)) > key(val):
            # go to left
            return contains(left(tree), val)
        else:
            # go to right
            return contains(right(tree), val)


def pop_max(tree):
    """
    Returns maximum element from the tree
    """
    if tree is None:
        return tree, None
    elif right(tree) is None:
        return left(tree), value(tree)
    else:
        # there is right side of current tree goto right side
        right_node, val = pop_max(right(tree))
        return set_right(tree, right_node), val


def pop_min(tree):
    """
    Returns minimum element from the tree
    """
    if tree is None:
        return tree, None
    elif left(tree) is None:
        return right(tree), value(tree)
    else:
        # there is right side of current tree goto right side
        left_node, val = pop_min(left(tree))
        return set_left(tree, left_node), val


def pop(tree, val, key=_key_func):
    """
    Removes value from given tree
    """
    if tree is None:
        return tree, None
    elif key(value(tree)) == key(val):
        if left(tree):
            left_node, new_val = pop_max(left(tree))
            return make_node(left_node, new_val, right(tree)), val
        else:
            return right(tree), val
    elif key(value(tree)) > key(val):
        # goto left
        left_tree = left(tree)
        left_node, new_val = pop(left_tree, val, key=key)
        # if left tree is not changed return original tree
        if left_tree != left_node:
            return set_left(tree, left_node), new_val
        else:
            return tree, new_val
    else:
        # goto right
        right_tree = right(tree)
        right_node, new_val = pop(right_tree, val, key=key)
        # if right_tree is not changed return original tree
        if right_tree != right_node:
            return set_right(tree, right_node), new_val
        else:
            return tree, new_val
