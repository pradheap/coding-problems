import unittest

from linked_list_find_nth_node_from_end.source \
    import find_nth_node_from_end

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class TestLinkedListFindNthNodeFromEnd(unittest.TestCase):
    def test_with_empty_linked_list(self):
        node = find_nth_node_from_end(None, 2)

        self.assertIsNone(node)
    
    def test_with_one_node_and_bigger_k(self):
        node = find_nth_node_from_end(Node(3), 2)

        self.assertIsNone(node)
    
    def test_with_one_node_and_k_1(self):
        node = find_nth_node_from_end(Node(3), 1)

        self.assertEqual(node.data, 3)
    
    def test_with_k_0(self):
        node = find_nth_node_from_end(Node(3, Node(2)), 0)

        self.assertIsNone(node)
    
    def test_with_k_middle_node(self):
        node = find_nth_node_from_end(Node(1, Node(2, Node(3))), 2)

        self.assertEqual(node.data, 2)
    
    def test_with_k_equal_to_linked_list_size(self):
        node = find_nth_node_from_end(Node(1, Node(2, Node(3,  Node(4)))), 4)

        self.assertEqual(node.data, 1)
    
    def test_with_an_arbitrary_k(self):
        node = find_nth_node_from_end(Node(1, Node(2, Node(3,  Node(4, 
            Node(5, Node(6, )))))), 4)

        self.assertEqual(node.data, 3)