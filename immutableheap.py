"""
An heap implementation that uses immutable nodes.
h = None  # empty node
h = push(h, value) # add value to heap.
count(h) # get element count of heap.
(h, poped_value) = pop(h) # remove head and return new heap
"""

import logging

logger = logging.getLogger(__name__)
# if there is no handler run this code
if not logger.handlers:
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    logger.addHandler(ch)


def compare(a, b):
    """
    Compare function in a consistent tree
    compare(parent, child) is True
    """
    return a > b


def left(node):
    """
    get left branch of given node
    """
    return node[0]


def set_left(node, left_node):
    """
    set left branch of given node
    """
    return (left_node,
            node[1],
            node[2],
            (1 + count(left_node) + count(node[2])))


def right(node):
    """
    get right branch of given node
    """
    return node[2]


def set_right(node, right_node):
    """
    set right branch of given node
    """
    return (node[0],
            node[1],
            right_node,
            (1 + count(node[0]) + count(right_node)))


def value(node):
    """
    get value of given node
    """
    return node[1]


def set_value(node, value):
    """
    set vlaue of given node
    """
    return(node[0], value, node[2], node[3])


def make_node(left, value, right):
    """
    Creates a new node
    """
    return (left, value, right, (1 + count(left) + count(right)))


def update_value(node, val):
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


def count(node):
    """
    return length of current heap
    """
    if not node:
        result = 0
    else:
        result = node[3]
    return result


def is_leaf(node):
    """
    check if current node is a leaf
    """
    # return not left(node) and not right(node)
    return count(node) == 1


def push(node, val):
    """
    Add a new value to heap.
    Addes to value as a branch than switches added branch
    with its parent if needed.(push and swim)
    """
    if not node:
        node = make_node(None, val, None)
    else:
        # push new value to smaller branch
        if count(left(node)) <= count(right(node)):
            child = left(node)
            set_fun = set_left
            # logger.debug('goto_left')
        else:
            child = right(node)
            set_fun = set_right
            # logger.debug('goto_right')

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

    if count(left(node)) > count(right(node)):
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


def pop(node):
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
