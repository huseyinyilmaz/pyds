import random
import unittest
import node
import persistentbst as bst


class TestImmutableHeap(unittest.TestCase):
    SIZE = 100

    def test_enter_smaller_value(self):
        t = bst.push(None, 5)
        t = bst.push(t, 3)
        left = node.make_node(None, 3, None)
        expected = node.make_node(left, 5, None)
        self.assertEqual(t, expected)
        self.assertEqual(node.count(t), 2)

    def test_enter_larger_value(self):
        t = bst.push(None, 3)
        print t

        t = bst.push(t, 5)
        print t
        right = node.make_node(None, 5, None)
        expected = node.make_node(None, 3, right)
        self.assertEqual(t, expected)
        self.assertEqual(node.count(t), 2)

    def test_contains(self):
        for i in range(100):
            print i
