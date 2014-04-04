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
        t = bst.push(t, 5)
        right = node.make_node(None, 5, None)
        expected = node.make_node(None, 3, right)
        self.assertEqual(t, expected)
        self.assertEqual(node.count(t), 2)

    def test_contains(self):
        values = [10, 5, 15, 3, 7, 13, 17, 20, 1]
        not_values = [2, 4, 6, 8, 11, 18, 21]
        t = None
        for val in values:
            t = bst.push(t, val)

        for val in values:
            self.assertTrue(bst.contains(t, val))
        for val in not_values:
            self.assertFalse(bst.contains(t, val))

    def test_pop_max(self):
        values = [10, 5, 15, 3, 7, 13, 17, 20, 1]
        t = None
        for val in values:
            t = bst.push(t, val)
        # pop back all values
        sorted_values = sorted(values, reverse=True)
        for expected_val in sorted_values:
            t, max_val = bst.pop_max(t)
            self.assertEqual(max_val, expected_val)
        # make sure that whole tree is empty
        self.assertIs(t, None)
        # check if we pop from empty tree result is None
        self.assertEqual(bst.pop_max(None), (None, None))

    def test_pop_min(self):
        values = [10, 5, 15, 3, 7, 13, 17, 20, 1]
        t = None
        for val in values:
            t = bst.push(t, val)

        # pop back all values
        sorted_values = sorted(values)
        for expected_val in sorted_values:
            t, min_val = bst.pop_min(t)
            self.assertEqual(min_val, expected_val)
        # make sure that whole tree is empty
        self.assertIs(t, None)
        # check if we pop from empty tree result is None
        self.assertEqual(bst.pop_max(None), (None, None))

    def test_pop(self):
        values = [10, 5, 15, 3, 7, 13, 17, 20, 1]
        not_values = [2, 4, 6, 8, 11, 18, 21]
        t = None

        for val in values:
            t = bst.push(t, val)

        for val in not_values:
            self.assertEqual(bst.pop(t, val), (t, None))

        # pop back all values
        shuffled_values = values[:]
        random.shuffle(shuffled_values)
        for expected_val in shuffled_values:
            t, new_val = bst.pop(t, expected_val)
            self.assertEqual(new_val, expected_val)
        # make sure that whole tree is empty
        self.assertIs(t, None)
        # check if we pop from empty tree result is None
        self.assertEqual(bst.pop(None, 5), (None, None))
