import unittest

from array_max_consecutive_ones.source import count_1s


class TestMaxCountOfConsecutiveOnes(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_1s([]), 0)

    def test_one_one_at_end(self):
        self.assertEqual(count_1s([0, 0, 1]), 1)

    def test_one_one_at_start(self):
        self.assertEqual(count_1s([1, 0, 0]), 1)
    
    def test_multiple_ones_at_end(self):
        self.assertEqual(count_1s([0, 0, 1, 1, 1, 1]), 4)

    def test_multiple_ones_at_start(self):
        self.assertEqual(count_1s([1, 1, 1, 0, 0]), 3)
    
    def test_multiple_interleaving_ones(self):
        self.assertEqual(count_1s([1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1]), 4)
