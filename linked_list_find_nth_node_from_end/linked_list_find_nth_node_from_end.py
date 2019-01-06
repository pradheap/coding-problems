
def find_nth_node_from_end(head, k):
    kth_node = None
    curr = head

    i = 0
    while curr is not None and i < k:
        curr = curr.next
        i += 1
    
    # If i == k, then k is < size of the linked list.
    # Now, assign the head to the kth node.
    if i == k:
        kth_node = head
    
    while curr is not None:
        kth_node = kth_node.next
        curr = curr.next
    
    return kth_node