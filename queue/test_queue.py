import unittest

from queue.queue import Queue

class TestQueue(unittest.TestCase):

    def test_enqueue_elements(self):
        q = Queue()
        q.enqueue(2)
        q.enqueue('R')

        self.assertEqual(q.size(), 2)
    
    def test_empty_queue_dequeue(self):
        q = Queue()

        self.assertIsNone(q.dequeue())
    
    def test_empty_queue_peek(self):
        q = Queue()

        self.assertIsNone(q.peek())

    def test_enqueue_and_dequeue_equal_element(self):
        q = Queue()

        q.enqueue(2)
        q.enqueue(3)
        q.enqueue('R')

        q.dequeue()
        q.dequeue()
        q.dequeue()

        self.assertEqual(q.size(), 0)
    
    def test_peek_very_first_element(self):
        q = Queue()

        q.enqueue(0)
        q.enqueue(1)

        self.assertEqual(q.peek(), 0)
    
    def test_deque_element(self):
        q = Queue()
        q.enqueue(20)
        q.enqueue('R')

        self.assertEqual(q.dequeue(), 20)
