
class Stack:
    def __init__(self):
        self._store = []
    
    def push(self, data):
        self._store.append(data)
    
    def pop(self):
        if len(self._store) > 0:
            return self._store.pop()
        return None
    
    def peek(self):
        if len(self._store) > 0:
            return self._store[len(self._store) - 1]
        return None
    
    def size(self):
        return len(self._store)
