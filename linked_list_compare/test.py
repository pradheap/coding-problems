import unittest

from linked_list_compare.source import compare


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class TestCompareLinkedLists(unittest.TestCase):

    def test_compare_with_both_lists_as_none(self):
        self.assertFalse(compare(None, None))

    def test_compare_with_one_list_as_none(self):
        self.assertFalse(compare(Node(4, Node(3)), None))

    def test_compare_same_lists_with_single_node(self):
        self.assertTrue(compare(Node(4), Node(4)))

    def test_compare_same_lists_with_multiple_nodes(self):
        self.assertTrue(
            compare(
                    Node(4, Node(5, Node(6, Node(7)))), 
                    Node(4, Node(5, Node(6, Node(7))))
                )
        )

    def test_compare_different_lists_with_single_node(self):
        self.assertFalse(compare(Node(4), Node(0)))

    def test_compare_different_lists_with_multiple_nodes(self):
        self.assertFalse(
            compare(
                    Node(4, Node('5', Node(6, Node(7)))), 
                    Node(4, Node(5, Node(6, Node(7))))
                )
        )
