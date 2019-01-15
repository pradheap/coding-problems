import unittest

from linked_list_is_palindrome.source import is_palindrome


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class TestLinkedListIsPalindrome(unittest.TestCase):
    def test_with_none(self):
        self.assertFalse(is_palindrome(None))

    def test_with_odd_nodes_palindrome(self):
        head = Node(4, Node(5, Node(7, Node(5, Node(4)))))
        self.assertTrue(is_palindrome(head))
    
    def test_with_odd_nodes_non_palindrome(self):
        head = Node(4, Node(5, Node(7, Node(9, Node(11)))))
        self.assertFalse(is_palindrome(head))
    
    def test_with_even_nodes_non_palindrome(self):
        head = Node(4, Node(5, Node(7, Node(9))))
        self.assertFalse(is_palindrome(head))
    
    def test_with_even_nodes_palindrome(self):
        head = Node(4, Node(5, Node(5, Node(4))))
        self.assertTrue(is_palindrome(head))
    
    def test_with_minimum_even_nodes_palindrome(self):
        head = Node(4, Node(4))
        self.assertTrue(is_palindrome(head))
    
    def test_with_minimum_even_nodes_non_palindrome(self):
        head = Node(4, Node(5))
        self.assertFalse(is_palindrome(head))
    
    def test_with_minimum_odd_nodes_palindrome(self):
        head = Node(4)
        self.assertTrue(is_palindrome(head))

    def test_with_minimum_odd_nodes_palindrome_1(self):
        head = Node(4, Node(9, Node(4)))
        self.assertTrue(is_palindrome(head))
    
    def test_with_minimum_odd_nodes_non_palindrome_1(self):
        head = Node(4, Node(9, Node(14)))
        self.assertFalse(is_palindrome(head))
