
import unittest

from linked_list_middle_node.source import get_middle_node

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class TestGetMiddleNode(unittest.TestCase):
    def test_with_empty_list(self):
        self.assertIsNone(get_middle_node(None), None)

    def test_single_node(self):
        head = Node(4)
        self.assertEqual(get_middle_node(head).data, 4)
    
    def test_two_nodes(self):
        head = Node(4, Node(5))
        self.assertEqual(get_middle_node(head).data, 4)
    
    def test_odd_number_of_nodes(self):
        head = Node(4, Node(5, Node(9)))
        self.assertEqual(get_middle_node(head).data, 5)
    
    def test_even_number_of_nodes(self):
        head = Node(4, Node(5, Node(9, Node(8))))
        self.assertEqual(get_middle_node(head).data, 5)
