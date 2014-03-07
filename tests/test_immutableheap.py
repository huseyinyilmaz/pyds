import random
import unittest

import immutableheap


class TestImmutableHeap(unittest.TestCase):
    SIZE = 1000

    def setUp(self):
        pass

    def test_enter_smaller_value(self):
        h = immutableheap.push(None, 5)
        h = immutableheap.push(h, 3)
        self.assertEqual(immutableheap.count(h), 2)

    def test_enter_larger_value(self):
        h = immutableheap.push(None, 3)
        h = immutableheap.push(h, 5)
        self.assertEqual(immutableheap.count(h), 2)

    def test_push(self):
        count = self.SIZE
        head = count - 1
        h = None
        for i in range(count):
            h = immutableheap.push(h, i)
        self.assertEqual(immutableheap.count(h), count)
        self.assertEqual(immutableheap.value(h), head)

    def test_pop(self):
        h = None
        for i in range(self.SIZE):
            h = immutableheap.push(h, i)
        for i in reversed(range(self.SIZE)):
            h, val = immutableheap.pop(h)
            self.assertEqual(val, i)
        self.assertIsNone(h)

    def test_sort(self):
        sample_list = [random.randint(1, 100000) for i in range(self.SIZE)]
        h = None
        for i in sample_list:
            h = immutableheap.push(h, i)

        sorted_list = sorted(sample_list, reverse=True)
        for i in sorted_list:
            h, val = immutableheap.pop(h)
            self.assertEqual(val, i)
        self.assertIsNone(h)

if __name__ == '__main__':
    unittest.main()
