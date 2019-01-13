import unittest

from linked_list_merge.source import merge_lists, Node

def linked_list_to_list(head):
    list = []
    curr = head
    while curr is not None:
        list.append(curr.data)
        curr = curr.next
    return list


class TestLinkedListMerge(unittest.TestCase):
    def test_merge_normal_lists(self):
        head1 = Node(20, Node(30, Node(40)))
        head2 = Node(12, Node(22, Node(101)))

        merged = merge_lists(head1, head2)

        self.assertEqual(linked_list_to_list(merged), [12, 20, 22, 30, 40, 101])
    
    def test_merge_normal_one_element_lists(self):
        head1 = Node(20)
        head2 = Node(12)

        merged = merge_lists(head1, head2)

        self.assertEqual(linked_list_to_list(merged), [12, 20])
    
    def test_merge_normal_first_long_second_short_list(self):
        head1 = Node(10, Node(30, Node(40)))
        head2 = Node(12)

        merged = merge_lists(head1, head2)

        self.assertEqual(linked_list_to_list(merged), [10, 12, 30, 40])
    
    def test_merge_normal_first_short_second_long_list(self):
        head1 = Node(10, Node(30))
        head2 = Node(8, Node(24, Node(44, Node(54, Node(90, Node(100))))))

        merged = merge_lists(head1, head2)

        self.assertEqual(linked_list_to_list(merged), [8, 10, 24, 30, 44, 54, 90, 100])
    
    def test_merge_empty_lists(self):
        merged = merge_lists(None, None)

        self.assertEqual(linked_list_to_list(merged), [])
    
    def test_merge_one_empty_lists(self):
        head1 = Node(10, Node(30, Node(40)))

        merged = merge_lists(head1, None)

        self.assertEqual(linked_list_to_list(merged), [10, 30, 40])
    
    def test_merge_lists_with_same_elements(self):
        head1 = Node(20, Node(30, Node(40)))
        head2 = Node(20, Node(30, Node(40)))

        merged = merge_lists(head1, head2)

        self.assertEqual(linked_list_to_list(merged), [20, 20, 30, 30, 40, 40])
