# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def reverse(head):
    if head is None:
        return head
    
    prev = None
    curr = head

    while curr is not None:
        next = curr.next
        curr.next = prev

        prev = curr
        curr = next

    return prev
