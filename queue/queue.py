from collections import deque

class Queue:
    def __init__(self):
        self._store = deque()
    
    def enqueue(self, data):
        self._store.append(data)
    
    def dequeue(self):
        if len(self._store) > 0:
            return self._store.popleft()
        return None
    
    def peek(self):
        if len(self._store) > 0:
            return self._store[0]
        return None
    
    def size(self):
        return len(self._store)