import random
import unittest

import persistentheap as heap


class TestImmutableHeap(unittest.TestCase):
    SIZE = 1000

    def setUp(self):
        pass

    def test_enter_smaller_value(self):
        h = heap.push(None, 5)
        h = heap.push(h, 3)
        self.assertEqual(heap.count(h), 2)

    def test_enter_larger_value(self):
        h = heap.push(None, 3)
        h = heap.push(h, 5)
        self.assertEqual(heap.count(h), 2)

    def test_push(self):
        count = self.SIZE
        head = count - 1
        h = None
        for i in range(count):
            h = heap.push(h, i)
        self.assertEqual(heap.count(h), count)
        self.assertEqual(heap.value(h), head)

    def test_pop(self):
        h = None
        for i in range(self.SIZE):
            h = heap.push(h, i)
        for i in reversed(range(self.SIZE)):
            h, val = heap.pop(h)
            self.assertEqual(val, i)
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

if __name__ == '__main__':
    unittest.main()
