import unittest

from array_search_insert_position.source import get_position


class TestGetPosition(unittest.TestCase):
    def test_search_position_in_unit_list(self):
        self.assertEqual(get_position([1], 1), 0)
    
    def test_insert_position_in_unit_list(self):
        self.assertEqual(get_position([1], 2), 1)
    
    def test_insert_position_in_normal_list(self):
        self.assertEqual(get_position([1, 3, 4], 2), 1)

    def test_search_position_in_normal_list(self):
        self.assertEqual(get_position([1, 5, 8], 8), 2)

    def test_insert_position_in_normal_list_beyond_last_element(self):
        self.assertEqual(get_position([1, 5, 8], 10), 3)
    
    def test_insert_position_in_normal_list_below_first_element(self):
        self.assertEqual(get_position([4, 5, 8], 3), 0)
