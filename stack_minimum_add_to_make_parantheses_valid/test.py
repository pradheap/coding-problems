import unittest

from stack_minimum_add_to_make_parantheses_valid.source import minimum_add


class TestMinimumAddToMakeParantheses(unittest.TestCase):
    def test_balanced_parantheses(self):
        self.assertEqual(minimum_add('()'), 0)
    
    def test_a_pair_of_balanced_parantheses(self):
        self.assertEqual(minimum_add('(())'), 0)
    
    def test_unbalanced_parantheses(self):
        self.assertEqual(minimum_add('('), 1)
        self.assertEqual(minimum_add(')'), 1)
    
    def test_unbalanced_pair_of_parantheses(self):
        self.assertEqual(minimum_add('(()'), 1)
        self.assertEqual(minimum_add('())'), 1)
    
    def test_multiple_pairs_of_unbalanced_parantheses(self):
        self.assertEqual(minimum_add('())))(('), 5)
        self.assertEqual(minimum_add('(((()()((('), 6)
