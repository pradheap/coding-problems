import unittest
from max_increase_skyline.source import max_increase_keeping_skyline

# From the question, 1 < grid.length = grid[0].length <= 50.
# Only square grids are allowed as input.
class TestMaxIncreaseSkyline(unittest.TestCase):
    def test_grid4x4(self):
        grid = [
            [3, 0, 8, 4], 
            [2, 4, 5, 7],
            [9, 2, 6, 3],
            [0, 3, 1, 0]
        ]
        self.assertEqual(35, max_increase_keeping_skyline(grid))

    def test_grid2x2(self):
        grid = [
            [3, 0], 
            [2, 4]
        ]
        self.assertEqual(4, max_increase_keeping_skyline(grid))
    
    def test_grid1x1(self):
        grid = [[1]]
        self.assertEqual(0, max_increase_keeping_skyline(grid))
    
    def test_grid1x2(self):
        grid = [[1, 2]]
        self.assertRaises(ValueError, max_increase_keeping_skyline, grid)
