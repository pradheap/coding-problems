
def is_palindrome(head):
    if head is None:
        return False
    
    if head.next is None:
        return True

    middle = head
    last = head.next
    while last and last.next:
        middle = middle.next
        last = last.next.next
    
    end_node = _reverse_nodes(middle)
    print(middle.data)
    left = head
    right = end_node

    while right and left:
        if right.data != left.data:
            return False
        right = right.next
        left = left.next

    _reverse_nodes(end_node)
    return True

def _reverse_nodes(head):
    prev = head
    curr = head.next
    if curr is None:
        return curr

    while curr:
        next_next = curr.next
        curr.next = prev

        prev = curr
        curr = next_next

    head.next = None
    return prev
