import unittest

from matrix_flip_an_image.source import flip_image

class TestMatrixFlip(unittest.TestCase):
    def test_empty_matrix(self):
        matrix = [[]]

        self.assertListEqual(flip_image(matrix), [[]])
    
    def test_1x1_matrix(self):
        matrix = [[1]]

        self.assertListEqual(flip_image(matrix), [[0]])
    
    def test_3x1_matrix(self):
        matrix = [[1], [0], [1]]

        self.assertListEqual(flip_image(matrix), [[0], [1], [0]])
    
    def test_3x3_matrix(self):
        matrix = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]

        self.assertListEqual(
            flip_image(matrix), [[1, 0, 0], [0, 1, 0], [1, 1, 1]])
