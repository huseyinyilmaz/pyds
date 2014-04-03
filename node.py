"""
Node manipulation functions.

"""


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


def make_node(left, value, right):
    """
    Creates a new node
    """
    return (left, value, right, (1 + count(left) + count(right)))
