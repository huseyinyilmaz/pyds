def make_node(left, value, right):
    """
    Creates a new node
    """
    return (left, value, right)


def _compare(a, b):
    """
    Compare function.
    In a consistent tree:
        compare(parent, right(parent)) is True
        compare(parent, left(parent)) is True

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
    return make_node(left_node, node[1], node[2])


def right(node):
    """
    get right branch of given node
    """
    return node[2]


def set_right(node, right_node):
    """
    set right branch of given node
    """
    return make_node(node[0],
                     node[1],
                     right_node)


def value(node):
    """
    get value of given node
    """
    return node[1]


def set_value(node, val):
    """
    set vlaue of given node
    """
    return make_node(node[0], value, node[2])


def push(tree, val, compare=_compare):
    if tree is None:
        return make_node(None, val, None)
    else:
        parent_val = value(tree)
        if compare(parent_val, val):
            None
