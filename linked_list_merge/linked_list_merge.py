
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def merge_lists(head1, head2):
    
    """ Merge two sorted linked lists.
    :param head1: head of the first linked list.
    :param head2: head of the second linked list.

    """
    if head1 is None:
        return head2
    elif head2 is None:
        return head1

    # Temporary sentinel node for the very first node
    # Avoid special logic for setting up the head of the merged lists
    # with whichever node is the smallest.
    new_ll_head = Node(None)
    new_ll_node = new_ll_head

    a_list_node = head1
    b_list_node = head2

    while a_list_node is not None and b_list_node is not None:
        if a_list_node.data < b_list_node.data:
            new_ll_node.next = Node(a_list_node.data)
            a_list_node = a_list_node.next
        else:
            new_ll_node.next = Node(b_list_node.data)
            b_list_node = b_list_node.next

        new_ll_node = new_ll_node.next
    
    if a_list_node is None:
        new_ll_node.next = b_list_node
    elif b_list_node is None:
        new_ll_node.next = a_list_node

    return new_ll_head.next
