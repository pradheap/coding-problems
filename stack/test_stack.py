import unittest

from stack.stack import Stack

class TestStack(unittest.TestCase):
    def test_stack_add_elements(self):
        stack = Stack()
        stack.push(2)

        self.assertEqual(stack.size(), 1)
    
    def test_push_pop_single_element(self):
        stack = Stack()
        stack.push(2)
        stack.pop()

        self.assertEqual(stack.size(), 0)
    
    def test_peek_single_element(self):
        stack = Stack()
        stack.push(2)

        self.assertEqual(stack.peek(), 2)
    
    def test_peek_empty_stack(self):
        stack = Stack()

        self.assertIsNone(stack.peek())
    
    def test_pop_empty_stack(self):
        stack = Stack()

        self.assertIsNone(stack.pop())
    
    def test_pop_last_inserted_element(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)

        self.assertEqual(stack.pop(), 30)
    
    def test_peek_last_inserted_element(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)

        self.assertEqual(stack.peek(), 30)
