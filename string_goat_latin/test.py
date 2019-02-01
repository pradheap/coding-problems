import unittest

from string_goat_latin.source import goat_latin


class TestGoatLatin(unittest.TestCase):
    def test_famous_two_words(self):
        self.assertEqual(goat_latin('Hello World'), 'elloHmaa orldWmaaa')
    
    def test_one_word_first_letter_consonant(self):
        self.assertEqual(goat_latin('Hello'), 'elloHmaa')
        self.assertEqual(goat_latin('hello'), 'ellohmaa')
    
    def test_one_word_first_letter_vowel(self):
        self.assertEqual(goat_latin('Apple'), 'Applemaa')
        self.assertEqual(goat_latin('apple'), 'applemaa')
    
    def test_long_sentences(self):
        self.assertEqual(
            goat_latin('I speak Goat Latin'), 
            'Imaa peaksmaaa oatGmaaaa atinLmaaaaa'
        )
        self.assertEqual(
            goat_latin('The quick brown fox jumped over the lazy dog'),
            'heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa ' +
            'hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa'
        )
