
def remove_duplicates(head):
    if head is None or head.next is None:
        return head

    prev = head
    curr = head.next
    while curr is not None:
        if prev.data != curr.data:
            prev = prev.next

        curr = curr.next
        # Set the prev's next to curr elem to account for a case where
        # all the nodes in a LL contains the same data as seen in the test.
        prev.next = curr

    return head
