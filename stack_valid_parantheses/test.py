import unittest

from stack_valid_parantheses.source import is_valid


class TestValidParantheses(unittest.TestCase):
    def test_empty_string(self):
        self.assertFalse(is_valid(''))

    def test_single_opening_bracket(self):
        self.assertFalse(is_valid('['))
    
    def test_single_closing_bracket(self):
        self.assertFalse(is_valid(']'))
    
    def test_single_pair_of_brackets(self):
        self.assertTrue(is_valid('[]'))
    
    def test_triple_pairs_of_valid_brackets(self):
        self.assertTrue(is_valid('[{()}]'))
    
    def test_missing_one_opening_bracket(self):
        self.assertFalse(is_valid('[()}]'))

    def test_missing_one_closing_bracket(self):
        self.assertFalse(is_valid('[(]'))
    
    def test_multiple_same_brackets(self):
        self.assertTrue(is_valid('[[[]]]'))
