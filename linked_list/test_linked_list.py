import unittest

from linked_list.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def test_linked_list_add(self):

        ll = LinkedList()
        ll.add(2)

        self.assertEqual(str(ll), '2')
    
    def test_linked_list_remove(self):

        ll = LinkedList()
        ll.add(2)
        ll.remove()

        self.assertEqual(str(ll), '')
    
    def test_empty_linked_list_remove(self):

        ll = LinkedList()
        ll.remove()

        self.assertEqual(str(ll), '')
    
    def test_empty_linked_list_size(self):

        ll = LinkedList()

        self.assertEqual(ll.size(), 0)
    
    def test_linked_list_size(self):

        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)

        self.assertEqual(ll.size(), 3)
    
    def test_empty_linked_list_find(self):

        ll = LinkedList()

        self.assertFalse(ll.find(43))
    
    def test_linked_list_find_not_existing_element(self):

        ll = LinkedList()
        ll.add(20)
        ll.add(2)
        ll.add(3)

        self.assertFalse(ll.find(43))
    
    def test_linked_list_find_existing_element(self):

        ll = LinkedList()
        ll.add(20)
        ll.add(2)
        ll.add(3)

        self.assertTrue(ll.find(2))
    