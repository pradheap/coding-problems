import unittest

from string_run_length_encoding.source import encode


class TestRunLengthEncoding(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(encode(''), '')
    
    def test_abc(self):
        self.assertEqual(encode('abc'), 'a1b1c1')
    
    def test_single_char(self):
        self.assertEqual(encode('f'), 'f1')
    
    def test_single_repeated_char(self):
        self.assertEqual(encode('ffffff'), 'f6')
    
    def test_multiple_repeated_char(self):
        self.assertEqual(encode('affrraaccdswww'), 'a1f2r2a2c2d1s1w3')
