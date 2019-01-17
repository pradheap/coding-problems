import unittest

from array_sort_by_odd_even.source import sort_by_parity


class TestSortByParity(unittest.TestCase):
    def test_empty_list(self):
        arr = []

        sort_by_parity([])

        self.assertEqual([], [])
    
    def test_single_element_list(self):
        arr = [4]

        sort_by_parity(arr)

        self.assertEqual(arr, arr)
    
    def test_two_elements_already_sorted_list(self):
        arr = [1, 4]

        sort_by_parity(arr)

        self.assertEqual(arr, arr)
    
    def test_multiple_elements_already_sorted_list(self):
        arr = [1, 3, 5, 2, 4]

        sort_by_parity(arr)

        self.assertEqual(arr, arr)

    def test_two_elements_unsorted_list(self):
        arr = [4, 1]

        sort_by_parity(arr)

        self.assertEqual(arr, [1, 4])
    
    def test_multiple_elements_unsorted_list(self):
        arr = [1, 2, 3, 4, 5]

        sort_by_parity(arr)

        # [1, 5, 3, 4, 2] is one of the order, it could also be [1, 3, 5, 2, 4]
        self.assertEqual(arr, [1, 5, 3, 4, 2])
    
    def test_odd_only_list(self):
        arr = [1, 7, 3, 11, 5]

        sort_by_parity(arr)

        self.assertEqual(arr, arr)
    
    def test_even_only_list(self):
        arr = [2, 6, 10, 4]

        sort_by_parity(arr)

        self.assertEqual(arr, arr)
