from linked_list import *

def reverse(head: LinkedList) -> LinkedList:
    prev_node = None
    while head:
        next_node = head.next
        head.next = prev_node
        prev_node = head
        head = next_node
    return prev_node



def test_reverse_empty_list():
    head = None
    reversed_head = reverse(head)
    assert list_to_array(reversed_head) == []

def test_reverse_single_element_list():
    head = LinkedList(1)
    reversed_head = reverse(head)
    assert list_to_array(reversed_head) == [1]

def test_reverse_multiple_elements_list():
    head = create_list_from_array([1, 2, 3, 4, 5])
    reversed_head = reverse(head)
    assert list_to_array(reversed_head) == [5, 4, 3, 2, 1]
