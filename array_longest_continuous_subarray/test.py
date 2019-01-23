import unittest

from array_longest_continuous_subarray.source import subarray


class TestLongestContinuousSubarray(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(subarray([]), 0)

    def test_single_element_list(self):
        self.assertEqual(subarray([1]), 1)

    def test_same_elements_list(self):
        self.assertEqual(subarray([5, 5, 5 ,5 ,5 ,5]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(subarray([1, 2, 3, 3, 2, 6, 8, 10, 3]), 4)
    
    def test_multiple_same_length_subarrays_list(self):
        self.assertEqual(subarray([1, 4, 1, 2, 1, 8, 1, 3]), 2)
    
    def test_multiple_negative_elements_list(self):
        self.assertEqual(subarray([-1, -4, -1, 2, 4, 3, 0, 1, 3]), 4)
