
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def add_two_numbers(head1, head2):
    curr1 = head1
    curr2 = head2
    if curr1 is None or curr2 is None:
        return curr1 or curr2
    
    result = Node(None)
    head = result
    to_carry = 0
    while curr1 or curr2 or to_carry:
        sum = 0
        if curr1:
            sum += curr1.data
        if curr2:
            sum += curr2.data
        if to_carry:
            sum += to_carry
            to_carry = 0
        if sum > 9:
            to_carry = 1
            sum = sum % 10

        head.next = Node(sum)
        head = head.next
        curr1 = curr1.next if curr1 else None
        curr2 = curr2.next if curr2 else None

    return result.next
