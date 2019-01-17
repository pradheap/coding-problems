import unittest

from array_two_sum_sorted.source import indices_for_two_sum, indices_for_two_sum_v1

class TestArrayTwoSum(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(indices_for_two_sum([], 9))
    
    def test_single_element_list(self):
        self.assertIsNone(indices_for_two_sum([1], 9))
    
    def test_two_elements_list(self):
        self.assertIsNone(indices_for_two_sum([2, 3], 9))
    
    def test_multiple_elements_list(self):
        self.assertIsNone(indices_for_two_sum([1, 2, 3, 4, 7, 9], 14))
    
    def test_two_elements_list_equal_to_sum(self):
        self.assertTupleEqual(indices_for_two_sum([2, 3], 5), (0, 1))
    
    def test_multiple_elements_list_equal_to_sum(self):
        self.assertTupleEqual(indices_for_two_sum([1, 2, 3, 4, 7, 9], 9), (1, 4))


class TestArrayTwoSumV1(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(indices_for_two_sum_v1([], 9))
    
    def test_single_element_list(self):
        self.assertIsNone(indices_for_two_sum_v1([1], 9))
    
    def test_two_elements_list(self):
        self.assertIsNone(indices_for_two_sum_v1([2, 3], 9))
    
    def test_multiple_elements_list(self):
        self.assertIsNone(indices_for_two_sum_v1([1, 2, 3, 4, 7, 9], 14))
    
    def test_two_elements_list_equal_to_sum(self):
        self.assertTupleEqual(indices_for_two_sum_v1([2, 3], 5), (0, 1))
    
    def test_multiple_elements_list_equal_to_sum(self):
        self.assertTupleEqual(indices_for_two_sum_v1([1, 2, 3, 4, 7, 9], 9), (1, 4))
