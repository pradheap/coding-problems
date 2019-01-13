import unittest

from linked_list_remove_duplicate_nodes.source import remove_duplicates


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def linkedlist_to_array(head):
    arr = []
    if head is None:
        return arr
    
    curr = head
    while curr is not None:
        arr.append(curr.data)
        curr = curr.next

    return arr

class TestRemoveDuplicates(unittest.TestCase):
    def test_None(self):
        self.assertIsNone(remove_duplicates(None))

    def test_single_node_list(self):
        head = Node(5)
        self.assertEqual(head, remove_duplicates(head))
    
    def test_duplicate_multiple_nodes_asc(self):
        head = Node(3, Node(3, Node(5)))
        self.assertEqual(linkedlist_to_array(remove_duplicates(head)), [3, 5])
    
    def test_duplicate_multiple_nodes_desc(self):
        head = Node(5, Node(5, Node(2)))
        self.assertEqual(linkedlist_to_array(remove_duplicates(head)), [5, 2])
    
    def test_duplicate_two_nodes(self):
        head = Node(5, Node(5))
        self.assertEqual(linkedlist_to_array(remove_duplicates(head)), [5])
    
    def test_duplicate_all_nodes(self):
        head = Node(5, Node(5, Node(5, Node(5, Node(5, Node(5))))))
        self.assertEqual(linkedlist_to_array(remove_duplicates(head)), [5])
