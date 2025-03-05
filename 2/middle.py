from linked_list import *


def middle(head: LinkedList) -> LinkedList:
    fast_node = head
    slow_node = head
    while fast_node:
        if fast_node.next is None:
            return slow_node
        elif fast_node.next.next is None:
            return slow_node
        else:
            fast_node = fast_node.next.next
            slow_node = slow_node.next

    return slow_node

def get_node_value(node):
    return node.value if node else None

def test_single_element_list():
    head = LinkedList(1)
    middle_node = middle(head)
    assert get_node_value(middle_node) == 1

def test_two_elements_list():
    head = create_list_from_array([1, 2])
    middle_node = middle(head)
    assert get_node_value(middle_node) == 1

def test_even_length_list():
    head = create_list_from_array([1, 2, 3, 4, 5, 6])
    middle_node = middle(head)
    assert get_node_value(middle_node) == 3

def test_odd_length_list():
    head = create_list_from_array([1, 2, 3, 4, 5])
    middle_node = middle(head)
    assert get_node_value(middle_node) == 3

def test_empty_list():
    head = None
    middle_node = middle(head)
    assert get_node_value(middle_node) is None