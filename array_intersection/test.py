import unittest

from array_intersection.source import find_intersection, find_intersection_v1


class TestArrayIntersection(unittest.TestCase):
    def test_with_none(self):
        self.assertListEqual(find_intersection(None, None), [])

    def test_with_one_of_the_list_as_none(self):
        self.assertListEqual(find_intersection([1, 2], None), [])
    
    def test_one_or_both_empty_lists(self):
        self.assertListEqual(find_intersection([1, 2], []), [])
        self.assertListEqual(find_intersection([], [1]), [])

    def test_with_no_intersection_single_element_lists(self):
        self.assertListEqual(find_intersection([2], [1]), [])
    
    def test_with_no_intersection_multiple_elements(self):
        self.assertListEqual(find_intersection([2, 3, 5], [1, 4]), [])

    def test_with_intersecting_single_element_lists(self):
        self.assertListEqual(find_intersection([7], [7]), [7])
    
    def test_with_intersecting_single_element_lists_with_dupes(self):
        self.assertListEqual(find_intersection([9, 9, 9], [9, 9]), [9])

    def test_with_only_intersecting_multiple_element_lists(self):
        # assertCountEqual sorted(a) == sorted(b)
        # means the expected and actual list elements could be in an order.
        self.assertCountEqual(find_intersection([7, 9, 0], [0, 9, 7]), [0, 9, 7])

    def test_with_only_intersecting_multiple_element_lists_with_dupes(self):
        # assertCountEqual sorted(a) == sorted(b)
        # means the expected and actual list elements could be in an order.
        self.assertCountEqual(
            find_intersection([7, 7, 9, 9, 0], [0, 0, 9, 7, 7]), [0, 9, 7]
        )
    
    def test_with_intersecting_multiple_element_lists_with_dupes(self):
        # assertCountEqual sorted(a) == sorted(b)
        # means the expected and actual list elements could be in an order.
        self.assertCountEqual(
            find_intersection(
                [7, 7, 8, 9, 1, 9, 12], [10, 11, 8, 8, 8, 11, 9, 17, 7]
            ),
            [8, 9, 7]
        )
    
    def test_with_intersecting_single_element_vs_multiple_element_lists(self):
        # assertCountEqual sorted(a) == sorted(b)
        # means the expected and actual list elements could be in an order.
        self.assertCountEqual(
            find_intersection_v1(
                [7], [5, 6, 10, 11, 8, 8, 8, 11, 9, 17, 7]
            ),
            [7]
        )

class TestArrayIntersectionV1(unittest.TestCase):
    def test_with_none(self):
        self.assertListEqual(find_intersection_v1(None, None), [])

    def test_with_one_of_the_list_as_none(self):
        self.assertListEqual(find_intersection_v1([1, 2], None), [])
    
    def test_one_or_both_empty_lists(self):
        self.assertListEqual(find_intersection_v1([1, 2], []), [])
        self.assertListEqual(find_intersection_v1([], [1]), [])

    def test_with_no_intersection_single_element_lists(self):
        self.assertListEqual(find_intersection_v1([2], [1]), [])
    
    def test_with_no_intersection_multiple_elements(self):
        self.assertListEqual(find_intersection_v1([2, 3, 5], [1, 4]), [])

    def test_with_intersecting_single_element_lists(self):
        self.assertListEqual(find_intersection_v1([7], [7]), [7])
    
    def test_with_intersecting_single_element_lists_with_dupes(self):
        self.assertListEqual(find_intersection_v1([9, 9, 9], [9, 9]), [9])
    
    def test_with_only_intersecting_multiple_element_lists(self):
        # assertCountEqual sorted(a) == sorted(b)
        # means the expected and actual list elements could be in an order.
        self.assertCountEqual(find_intersection_v1([7, 9, 0], [0, 9, 7]), [0, 9, 7])

    def test_with_only_intersecting_multiple_element_lists_with_dupes(self):
        # assertCountEqual sorted(a) == sorted(b)
        # means the expected and actual list elements could be in an order.
        self.assertCountEqual(
            find_intersection_v1([7, 7, 9, 9, 0], [0, 0, 9, 7, 7]), [0, 9, 7]
        )
    
    def test_with_intersecting_multiple_element_lists_with_dupes(self):
        # assertCountEqual sorted(a) == sorted(b)
        # means the expected and actual list elements could be in an order.
        self.assertCountEqual(
            find_intersection_v1(
                [7, 7, 8, 9, 1, 9, 12], [10, 11, 8, 8, 8, 11, 9, 17, 7]
            ),
            [9, 7, 8]
        )
    
    def test_with_intersecting_single_element_vs_multiple_element_lists(self):
        # assertCountEqual sorted(a) == sorted(b)
        # means the expected and actual list elements could be in an order.
        self.assertCountEqual(
            find_intersection_v1(
                [7], [5, 6, 10, 11, 8, 8, 8, 11, 9, 17, 7]
            ),
            [7]
        )
    
    def test_with_intersecting_multiple_element_lists_with_dupes_v1(self):
        # assertCountEqual sorted(a) == sorted(b)
        # means the expected and actual list elements could be in an order.
        self.assertCountEqual(
            find_intersection_v1(
                [7, 7, 7, 8, 8, 8, 9, 9], [8, 8, 8, 7, 7, 7, 6, 6]
            ),
            [7, 8]
        )