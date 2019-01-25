import unittest

from string_is_permutation.source import is_permutation


class TestIsPermutation(unittest.TestCase):
    def test_with_two_same_strings(self):
        self.assertTrue(is_permutation('Hello', 'Hello'))
    
    def test_with_two_anagrams(self):
        self.assertTrue(is_permutation('cinema', 'iceman'))
    
    def test_with_reversed_strings(self):
        self.assertTrue(is_permutation('hello', 'olleh'))
    
    def test_with_different_strings_one_empty(self):
        self.assertFalse(is_permutation('hello', ''))
    
    def test_with_different_strings(self):
        self.assertFalse(is_permutation('resist', 'resistance'))
