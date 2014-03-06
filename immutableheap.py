"""
An heap implementation that uses immutable nodes
"""


def compare(a, b):
    return a > b


def left(node):
    return node[0]


def set_left(node, left_node):
    return (left_node,
            node[1],
            node[2],
            (1 + count(left_node) + count(node[2])))


def right(node):
    return node[2]


def set_right(node, right_node):
    return (node[0],
            node[1],
            right_node,
            (1 + count(node[0]) + count(right_node)))


def value(node):
    return node[1]


def set_value(node, value):
    return(node[0], value, node[2], node[3])


def make_node(left, value, right):
    return (left, value, right, (1 + count(left) + count(right)))


def count(node):
    if not node:
        result = 0
    else:
        result = node[3]
    return result


def is_leaf(node):
    return not left(node) and not right(node)


def push(node, val):
    if not node:
        node = make_node(None, val, None)
    else:
        if count(left(node)) <= count(right(node)):
            child = left(node)
            set_fun = set_left
            print 'goto_left'
        else:
            child = right(node)
            set_fun = set_right
            print 'goto_right'
        child = push(child, val)

        if compare(value(child), value(node)):
            child_value = value(child)
            child = set_value(child, value(node))
            node = set_fun(node, child)
            node = set_value(node, child_value)

    return node


def pop_leaf(node):
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
    pass

# def balance(node):
#     val = value(node)
#     left_node = balance(left(node))
#     right_node = balance(right(node))
#     if value(left_node) > val:
#         val = value(left_node)
#         left_node = set_value(left_node)
