import unittest

from array_plus_one.source import plus_one


class TestArrayPlusOne(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(plus_one([]), [])

    def test_single_element_list(self):
        self.assertListEqual(plus_one([3]), [4])
    
    def test_single_element_list_as_0(self):
        self.assertListEqual(plus_one([0]), [1])
    
    def test_list_with_100(self):
        self.assertListEqual(plus_one([1, 0, 0]), [1, 0, 1])

    def test_double_element_list(self):
        self.assertListEqual(plus_one([3, 4]), [3, 5])

    def test_triple_element_list(self):
        self.assertListEqual(plus_one([1, 2, 3]), [1, 2, 4])

    def test_single_element_list_with_carry(self):
        self.assertListEqual(plus_one([9]), [1, 0])
    
    def test_double_element_list_with_carry(self):
        self.assertListEqual(plus_one([9, 9]), [1, 0, 0])

    def test_triple_element_list_with_carry(self):
        self.assertListEqual(plus_one([1, 2, 9]), [1, 3, 0])
