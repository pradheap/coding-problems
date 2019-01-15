
def get_middle_node(head):
    if head is None:
        return head

    middle = head
    last = head.next
    while last and last.next:
        middle = middle.next
        last = last.next.next
    
    return middle
