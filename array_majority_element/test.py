import unittest

from array_majority_element.source import majority_element, majority_element_v1


class TestMajorityElement(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(majority_element([]))
    
    def test_single_element_list(self):
        self.assertEqual(majority_element([1]), 1)
    
    def test_same_element_list(self):
        self.assertEqual(majority_element([1, 1]), 1)
    
    def test_odd_elements_list_with_majority(self):
        self.assertEqual(majority_element([1, 2, 1]), 1)
    
    def test_even_elements_list_with_majority(self):
        self.assertEqual(majority_element([1, 2, 2, 2]), 2)

    def test_odd_elements_list_with_no_majority(self):
        self.assertIsNone(majority_element([1, 2, 3]))
    
    def test_multiple_elements_list_with_majority(self):
        self.assertEqual(majority_element([1, 1, 2, 2, 3, 1, 1]), 1)
    
    def test_multiple_elements_list_with_majority_1(self):
        self.assertEqual(
            majority_element([4, 4, 4, 4, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]),
            4
        )


class TestMajorityElementV1(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(majority_element_v1([]))
    
    def test_single_element_list(self):
        self.assertEqual(majority_element_v1([1]), 1)
    
    def test_same_element_list(self):
        self.assertEqual(majority_element_v1([1, 1]), 1)
    
    def test_odd_elements_list_with_majority(self):
        self.assertEqual(majority_element_v1([1, 2, 1]), 1)
    
    def test_even_elements_list_with_majority(self):
        self.assertEqual(majority_element_v1([1, 2, 2, 2]), 2)

    def test_odd_elements_list_with_no_majority(self):
        self.assertIsNone(majority_element_v1([1, 2, 3]))
    
    def test_multiple_elements_list_with_majority(self):
        self.assertEqual(majority_element_v1([1, 1, 2, 2, 3, 1, 1]), 1)
    
    def test_multiple_elements_list_with_majority_1(self):
        self.assertEqual(
            majority_element_v1([4, 4, 4, 4, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]),
            4
        )
