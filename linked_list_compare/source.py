
def compare(head1, head2):
    if head1 is None or head2 is None:
        return False

    curr1, curr2 = head1, head2
    while curr1 is not None and curr2 is not None:
        if curr1.data != curr2.data:
            return False

        curr1 = curr1.next
        curr2 = curr2.next

    if curr1 is not None or curr2 is not None:
        return False

    return True
