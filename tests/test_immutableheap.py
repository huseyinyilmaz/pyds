import random
import unittest

import immutableheap


class TestImmutableHeap(unittest.TestCase):

    def setUp(self):
        pass

    def test_push(self):
        count = 1000
        head = count - 1
        h = None
        for i in range(count):
            h = immutableheap.push(h, i)

        self.assertEqual(immutableheap.count(h), count)
        self.assertEqual(immutableheap.value(h), head)


if __name__ == '__main__':
    unittest.main()
