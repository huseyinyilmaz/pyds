"""
A persistent heap implementation.
h = None  # empty node
h = push(h, value) # add value to heap.
count(h) # get element count of heap.
(h, poped_value) = pop(h) # remove head and return new heap

"""

from node import (left, set_left,
                  right, set_right,
                  value, set_value,
                  is_leaf, make_node)


def _compare(a, b):
    """
    Compare function.
    In a consistent tree:
        compare(parent, child) is True
    """
    return a > b


def get_complete_deepness(node):
    """
    Returns deepness of a complete binary tree.
    If tree branches is not complete or if they have
    different deepness level, function returns None.
    Only, if Both branches of tree has same deepness function will return an
    integer value.
    """
    if not node:
        result = 0
    else:
        left_deepness = get_complete_deepness(left(node))
        right_deepness = get_complete_deepness(right(node))

        if ((left_deepness == right_deepness) and
                (left_deepness is not None) and
                (right_deepness is not None)):
            result = left_deepness + 1
        else:
            result = None
    return result


def is_complete(node):
    "Check if given heap is a complete binary tree"
    return not node or bool(get_complete_deepness(node))


def is_consistent(node, compare=_compare):
    """
    Check if hash has a consistent state for given compare function.
    """
    if node is None:
        return True
    else:
        val = value(node)
        left_node = left(node)
        right_node = right(node)

        # if there is no left_node,
        # that means left branch is already consistent
        is_left_consistent = \
            (compare(val, value(left_node)) and
             is_consistent(left_node)) if left_node else True

        is_right_consistent = \
            (compare(val, value(right_node)) and
             is_consistent(right_node)) if right_node else True

        ## TODO make sure left and right branch has right deepness level
        return is_left_consistent and is_right_consistent


def update_value(node, val, compare=_compare):
    """
    updates value of a node.
    if childs are bigger than parent it switches child with parent
    """
    left_node = left(node)
    right_node = right(node)
    left_val = value(left_node) if left_node else None
    right_val = value(right_node) if right_node else None

    if left_node and compare(left_val, val):
        left_node = update_value(left_node, val)
        val = left_val

    if right_node and compare(right_val, val):
        right_node = update_value(right_node, val)
        val = right_val
    return make_node(left_node, val, right_node)


def is_add_to_left(node):
    """
    Decide if we should add next node to left or right branch
    """
    right_deepness = get_complete_deepness(right(node))
    left_deepness = get_complete_deepness(left(node))
    if right_deepness is None:
        # go to right
        result = False
    elif left_deepness is None:
        # go to left
        result = True
    elif left_deepness > right_deepness:
        result = False
    else:
        result = True

    return result


def is_pop_from_left(node):
    """
    Decides if we should pop next node from left branch or right branch
    """
    right_deepness = get_complete_deepness(right(node))
    left_deepness = get_complete_deepness(left(node))
    if right_deepness is None:
        # go to right
        result = False
    elif left_deepness is None:
        # go to left
        result = True
    elif left_deepness > right_deepness:
        result = True
    else:
        result = False

    return result


def push(node, val, compare=_compare):
    """
    Add a new value to heap.
    Addes to value as a branch than switches added branch
    with its parent if needed.(push and swim)
    """
    if not node:
        node = make_node(None, val, None)
    else:
        # push new value to smaller branch
        if is_add_to_left(node):
            child = left(node)
            set_fun = set_left
        else:
            child = right(node)
            set_fun = set_right

        child = push(child, val)

        if compare(value(child), value(node)):
            child_value = value(child)
            child = set_value(child, value(node))
            node = set_value(node, child_value)

        node = set_fun(node, child)
    return node


def pop_leaf(node):
    """
    pop last added leaf.
    pop_leaf(heap) -> (new_heap, poped_node)

    """
    if is_leaf(node):
        return None, node

    if is_pop_from_left(node):
        child = left(node)
        set_fun = set_left
    else:
        child = right(node)
        set_fun = set_right

    if is_leaf(child):
        node = set_fun(node, None)
        return (node, child)
    else:
        child, poped = pop_leaf(child)
        node = set_fun(node, child)
        return (node, poped)


def pop(node, compare=_compare):
    """
    pop head of the heap
    remove last added node
    add last added node as root node
    switch root with children if necessary.(sink last added node)
    pop(heap) -> (new_heap, value)
    """
    val = value(node)
    node, poped = pop_leaf(node)
    if node:
        node = update_value(node, value(poped))
    return node, val
