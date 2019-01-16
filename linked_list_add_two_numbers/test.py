import unittest

from linked_list_add_two_numbers.source import add_two_numbers


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def to_list(head):
    curr = head
    if head is None:
        return []
    
    res = []
    while curr is not None:
        res.append(curr.data)
        curr = curr.next
    
    return res

class TestLinkedListAddTwoNumbers(unittest.TestCase):
    def test_none_as_lists(self):
        self.assertIsNone(add_two_numbers(None, None))
    
    def test_one_list_as_none(self):
        head1 = Node(4)
        self.assertEqual(add_two_numbers(head1, None), head1)
        self.assertEqual(add_two_numbers(None, head1), head1)
    
    def test_single_digit(self):
        head1 = Node(3)
        head2 = Node(3)
        self.assertEqual(to_list(add_two_numbers(head1, head2)), [6])
    
    def test_single_digit_with_carry(self):
        head1 = Node(9)
        head2 = Node(7)
        self.assertEqual(to_list(add_two_numbers(head1, head2)), [6, 1])
    
    def test_double_digit(self):
        head1 = Node(3, Node(4))
        head2 = Node(3, Node(4))
        self.assertEqual(to_list(add_two_numbers(head1, head2)), [6, 8])
    
    def test_double_digit_with_carry(self):
        head1 = Node(9, Node(4))
        head2 = Node(9, Node(4))
        self.assertEqual(to_list(add_two_numbers(head1, head2)), [8, 9])
    
    def test_double_digit_with_carry_as_last(self):
        head1 = Node(9, Node(9))
        head2 = Node(9, Node(9))
        self.assertEqual(to_list(add_two_numbers(head1, head2)), [8, 9, 1])
    
    def test_double_digit_with_zeros(self):
        head1 = Node(0, Node(9, Node(9)))
        head2 = Node(9, Node(0, Node(1)))
        self.assertEqual(to_list(add_two_numbers(head1, head2)), [9, 9, 0, 1])
    
    def test_add_two_numbers_of_unequal_length(self):
        head1 = Node(0, Node(9, Node(9)))
        head2 = Node(9)
        self.assertEqual(to_list(add_two_numbers(head1, head2)), [9, 9, 9])
    
    def test_add_two_numbers_of_unequal_length_with_carry(self):
        head1 = Node(9, Node(9, Node(9)))
        head2 = Node(9)
        self.assertEqual(to_list(add_two_numbers(head1, head2)), [8, 0, 0, 1])

