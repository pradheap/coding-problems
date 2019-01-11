import unittest

from linked_list_odd_even_swap.source import odd_even_swap


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def return_data(head):
    curr = head

    data = []
    while curr is not None:
        data.append(curr.data)
        curr = curr.next

    return data

class TestOddEvenSwap(unittest.TestCase):

    def test_swapping_with_nothing(self):
        self.assertIsNone(odd_even_swap(None))

    def test_swapping_with_single_node(self):
        result = odd_even_swap(Node(3))

        self.assertEqual(return_data(result), [3])

    def test_swapping_with_single_odd_even_node(self):
        result = odd_even_swap(Node(3, Node(4)))

        self.assertEqual(return_data(result), [3, 4])

    def test_swapping_with_two_pairs_of_nodes(self):
        result = odd_even_swap(Node(1, Node(2, Node(3, Node(4)))))

        self.assertEqual(return_data(result), [1, 3, 2, 4])

    def test_swapping_with_four_pairs_of_nodes(self):
        result = odd_even_swap(Node(1, Node(2, Node(4, Node(3, Node(5, Node(6, Node(15, Node(16)))))))))

        self.assertEqual(return_data(result), [1, 4, 5, 15, 2, 3, 6, 16])

    def test_swapping_with_odd_number_of_nodes(self):
        result = odd_even_swap(Node(1, Node(2, Node(4))))

        self.assertEqual(return_data(result), [1, 4, 2])

    def test_swapping_with_odd_number_of_multiple_nodes(self):
        result = odd_even_swap(Node(1, Node(2, Node(4, Node(11, Node(21, Node(64, Node(88))))))))

        self.assertEqual(return_data(result), [1, 4, 21, 88, 2, 11, 64])
