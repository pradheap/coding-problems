import unittest

from matrix_is_toeplitz.source import is_toeplitz, is_toeplitz_v1


class TestMatrixIsToePlitz(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertFalse(is_toeplitz([[]]), [[]])

    def test_2X2_matrix(self):
        self.assertTrue(is_toeplitz([[1, 2], [2, 1]]))
    
    def test_2X4_matrix(self):
        self.assertTrue(is_toeplitz([[1, 2, 3, 4], [0, 1, 2, 3]]))

    def test_3X2_matrix(self):
        self.assertTrue(is_toeplitz([[1, 2], [0, 1], [-1, 0]]))
    
    def test_3X4_matrix(self):
        self.assertTrue(
            is_toeplitz([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]])
        )
    
    def test_4X4_matrix(self):
        self.assertTrue(
            is_toeplitz(
                [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2], [0, 9, 5, 1]]
            )
        )

class TestMatrixIsToePlitzV1(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertFalse(is_toeplitz_v1([[]]), [[]])

    def test_2X2_matrix(self):
        self.assertTrue(is_toeplitz_v1([[1, 2], [2, 1]]))
    
    def test_2X4_matrix(self):
        self.assertTrue(is_toeplitz_v1([[1, 2, 3, 4], [0, 1, 2, 3]]))

    def test_3X2_matrix(self):
        self.assertTrue(is_toeplitz_v1([[1, 2], [0, 1], [-1, 0]]))
    
    def test_3X4_matrix(self):
        self.assertTrue(
            is_toeplitz_v1([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]])
        )
    
    def test_4X4_matrix(self):
        self.assertTrue(
            is_toeplitz_v1(
                [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2], [0, 9, 5, 1]]
            )
        )
