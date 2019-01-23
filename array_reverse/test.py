import unittest

from array_reverse.source import reverse_array, reverse_array_v1

class TestArrayReverse(unittest.TestCase):
    def test_empty_list(self):
        arr = []

        reverse_array(arr)

        self.assertListEqual(arr, [])
    
    def test_unit_list(self):
        arr = [2]

        reverse_array(arr)

        self.assertListEqual(arr, [2])

    def test_two_elements_list(self):
        arr = [1, 2]

        reverse_array(arr)

        self.assertListEqual(arr, [2, 1])

    def test_multiple_elements_list(self):
        arr = [1, 2, 3, 5]

        reverse_array(arr)

        self.assertListEqual(arr, [5, 3, 2, 1])

class TestArrayReverseV1(unittest.TestCase):
    def test_empty_list(self):
        arr = []

        reverse_array_v1(arr)

        self.assertListEqual(arr, [])
    
    def test_unit_list(self):
        arr = [2]

        reverse_array_v1(arr)

        self.assertListEqual(arr, [2])

    def test_two_elements_list(self):
        arr = [1, 2]

        reverse_array_v1(arr)

        self.assertListEqual(arr, [2, 1])

    def test_multiple_elements_list(self):
        arr = [1, 2, 3, 5]

        reverse_array_v1(arr)

        self.assertListEqual(arr, [5, 3, 2, 1])
