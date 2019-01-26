import unittest

from array_squares_of_sorted_array.source import square


class TestSquares(unittest.TestCase):
    def test_with_single_element(self):
        self.assertListEqual(square([2]), [4])

    def test_with_two_element(self):
        self.assertListEqual(square([-2, 2]), [4, 4])
    
    def test_with_three_element(self):
        self.assertListEqual(square([-2, 0, 2]), [0, 4, 4])

    def test_with_multiple_element(self):
        self.assertListEqual(
            square([-9, -6, -3, 0, 2, 5, 9]), 
            [0, 4, 9, 25, 36, 81, 81]
        )
