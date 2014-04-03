import random
import unittest

import persistentheap as heap
import node

class TestImmutableHeap(unittest.TestCase):
    SIZE = 100

    def test_enter_smaller_value(self):
        h = heap.push(None, 5)
        h = heap.push(h, 3)
        self.assertEqual(node.count(h), 2)

    def test_enter_larger_value(self):
        h = heap.push(None, 3)
        h = heap.push(h, 5)
        self.assertEqual(node.count(h), 2)

    def test_push(self):
        count = self.SIZE
        head = count - 1
        h = None
        for i in range(count):
            h = heap.push(h, i)
            self.assertTrue(heap.is_consistent(h))

        self.assertEqual(node.count(h), count)
        self.assertEqual(node.value(h), head)

    def test_pop(self):
        h = None
        for i in range(self.SIZE):
            h = heap.push(h, i)
            self.assertTrue(heap.is_consistent(h))

        for i in reversed(range(self.SIZE)):
            h, val = heap.pop(h)
            self.assertEqual(val, i)
            self.assertTrue(heap.is_consistent(h))

        self.assertIsNone(h)

    def test_sort(self):
        sample_list = [random.randint(1, 100000) for i in range(self.SIZE)]
        h = None
        for i in sample_list:
            h = heap.push(h, i)

        sorted_list = sorted(sample_list, reverse=True)
        for i in sorted_list:
            h, val = heap.pop(h)
            self.assertEqual(val, i)
        self.assertIsNone(h)

    def test_is_complete(self):
        h = None
        self.assertTrue(heap.is_complete(h))

        for i in range(11):
            if i in [0, 1, 3, 7]:
                self.assertTrue(heap.is_complete(h))
            else:
                self.assertFalse(heap.is_complete(h))

            h = heap.push(h, i)

        self.assertFalse(heap.is_complete(h))

    def test_complete_branch_aware_adding(self):
        h = None
        h = heap.push(h, 1)
        self.assertTrue(heap.is_complete(h))
        self.assertTrue(heap.is_consistent(h))

        h = heap.push(h, 2)
        self.assertFalse(heap.is_complete(h))
        self.assertTrue(heap.is_complete(node.left(h)))
        self.assertIsNone(node.right(h))
        self.assertTrue(heap.is_consistent(h))

        h = heap.push(h, 3)
        self.assertTrue(heap.is_complete(h))
        self.assertTrue(heap.is_consistent(h))

        h = heap.push(h, 5)
        self.assertFalse(heap.is_complete(h))
        self.assertFalse(heap.is_complete(node.left(h)))
        self.assertTrue(heap.is_complete(node.right(h)))
        self.assertTrue(heap.is_consistent(h))


if __name__ == '__main__':
    unittest.main()
