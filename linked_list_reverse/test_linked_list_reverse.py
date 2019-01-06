import unittest

from linked_list_reverse.linked_list_reverse import reverse

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_to_list(head):
    list = []
    curr = head
    while curr is not None:
        list.append(curr.data)
        curr = curr.next
    return list

class TestLinkedListReverse(unittest.TestCase):

    def test_reverse_empty_linked_list(self):
        head = reverse(None)

        self.assertIsNone(head)
    
    def test_reverse_linked_list_one_node(self):
        reverse_head = reverse(Node(3))

        self.assertEqual(linked_list_to_list(reverse_head), [3])
    
    def test_reverse_linked_list(self):
        head = Node(1, Node(2, Node(3)))

        reverse_head = reverse(head)

        self.assertEqual(linked_list_to_list(reverse_head), [3, 2, 1])
    
    def test_reverse_linked_list_duplicate_data(self):
        head = Node(1, Node(1, Node(1)))

        reverse_head = reverse(head)

        self.assertEqual(linked_list_to_list(reverse_head), [1, 1, 1])
