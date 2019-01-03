import unittest


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def add(self, data):
        self.head = Node(data, self.head)
        self._size += 1
    
    def remove(self):
        if self.head is not None:
            self.head = self.head.next
            self._size -= 1
    
    def find(self, data):
        is_found = False
        curr = self.head

        while curr is not None and not is_found:
            if curr.data == data:
                is_found = True
            curr = curr.next

        return is_found
    
    def __str__(self):
        curr = self.head
        data = []
        while curr is not None:
            data.append(str(curr.data))
            curr = curr.next
        return ','.join(data)
    
    def size(self):
        return self._size
