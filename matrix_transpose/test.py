import unittest

from matrix_transpose.source import transpose_matrix


class TestTransposeMatrix(unittest.TestCase):
    def test_transpose_empty_list(self):
        self.assertListEqual(transpose_matrix([]), [])
    
    def test_transpose_empty_matrix(self):
        self.assertListEqual(transpose_matrix([[]]), [])
    
    def test_transpose_unit_matrix(self):
        self.assertListEqual(transpose_matrix([[0]]), [[0]])
    
    def test_transpose_2X2_matrix(self):
        self.assertListEqual(transpose_matrix([[0, 1], [2, 3]]), [[0, 2], [1, 3]])

    def test_transpose_3X2_matrix(self):
        self.assertListEqual(
            transpose_matrix(
                [[0, 1], [2, 3], [4, 5]]
            ), 
            [[0, 2, 4], [1, 3, 5]]
        )
    
    def test_transpose_2X3_matrix(self):
        self.assertListEqual(
            transpose_matrix(
                [[0, 1, 2], [3, 4, 5]]
            ), 
            [[0, 3], [1, 4], [2, 5]]
        )
