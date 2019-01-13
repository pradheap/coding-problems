
def odd_even_swap(head):
    if head is None or head.next is None:
        return head

    # 3 pointers, to keep track of odd node, even node and first even node.
    # curr_odd node's next will always be the first even node.
    odd = head
    first_even = head.next
    even = head.next

    while even is not None and even.next is not None:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = first_even
    return head
