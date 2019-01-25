import unittest

from array_merge_sorted_arrays.source import merge, merge_in_place


class TestMerge(unittest.TestCase):
    def test_merge_single_element_arrays(self):
        self.assertListEqual(merge([2], [3]), [2, 3])

    def test_merge_with_one_empty_array(self):
        self.assertListEqual(merge([2], []), [2])

    def test_merge_two_arrays_with_interleaving_elements(self):
        self.assertListEqual(
            merge([1, 5, 8, 9], [0, 2, 4, 7]), 
            [0, 1, 2, 4, 5, 7, 8, 9]
        )

    def test_merge_two_arrays_with_non_interleaving_elements(self):
        self.assertListEqual(
            merge([1, 5, 8, 9], [10, 12, 19]), 
            [1, 5, 8, 9, 10, 12, 19]
        )

    def test_merge_two_arrays_with_all_dupes(self):
        self.assertListEqual(
            merge([2, 2, 2, 2], [2, 2, 2]), 
            [2, 2, 2, 2, 2, 2, 2]
        )

    def test_merge_two_arrays_with_some_dupes(self):
        self.assertListEqual(
            merge([2, 2, 5, 7], [1, 4, 4, 6, 6, 9]), 
            [1, 2, 2, 4, 4, 5, 6, 6, 7, 9]
        )

class TestMergeInPlace(unittest.TestCase):
    def test_merge_single_element_arrays(self):
        arr1 = [2]
        merge_in_place(arr1, [3])

        self.assertListEqual(arr1, [2, 3])

    def test_merge_with_one_empty_array(self):
        arr1 = [2]
        merge_in_place(arr1, [])

        self.assertListEqual(arr1, [2])

    def test_merge_two_arrays_with_interleaving_elements(self):
        arr1 = [1, 5, 8, 9]
        merge_in_place(arr1, [0, 2, 4, 7])

        self.assertListEqual(arr1, [0, 1, 2, 4, 5, 7, 8, 9])

    def test_merge_two_arrays_with_non_interleaving_elements(self):
        arr1 = [1, 5, 8, 9]
        merge_in_place(arr1, [10, 12, 19])
        
        self.assertListEqual(arr1, [1, 5, 8, 9, 10, 12, 19])

    def test_merge_two_arrays_with_all_dupes(self):
        arr1 = [2, 2, 2, 2]
        merge_in_place(arr1, [2, 2, 2])
        
        self.assertListEqual(arr1, [2, 2, 2, 2, 2, 2, 2])

    def test_merge_two_arrays_with_some_dupes(self):
        arr1 = [2, 2, 5, 7]
        merge_in_place(arr1, [1, 4, 4, 6, 6, 9])
        
        self.assertListEqual(arr1, [1, 2, 2, 4, 4, 5, 6, 6, 7, 9])
