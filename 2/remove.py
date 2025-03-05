from linked_list import *


def remove(head: LinkedList, val: int) -> LinkedList:
    dummy_node = LinkedList(-1)
    dummy_node.next = head
    cur_node = head
    prev_node = dummy_node
    while cur_node:
        if cur_node.value == val:
            prev_node.next = cur_node.next
            if head == cur_node:
                head = cur_node.next
            del cur_node
            del dummy_node
            return head
        prev_node = cur_node
        cur_node = cur_node.next
    return head

def test_remove_from_empty_list():
    head = None
    head = remove(head, 1)
    assert list_to_array(head) == []

def test_remove_non_existent_value():
    head = create_list_from_array([1, 2, 3])
    head = remove(head, 4)
    assert list_to_array(head) == [1, 2, 3]

def test_remove_from_single_element_list():
    head = LinkedList(1)
    head = remove(head, 1)
    assert list_to_array(head) == []

def test_remove_first_element():
    head = create_list_from_array([1, 2, 3])
    head = remove(head, 1)
    assert list_to_array(head) == [2, 3]

def test_remove_last_element():
    head = create_list_from_array([1, 2, 3])
    head = remove(head, 3)
    assert list_to_array(head) == [1, 2]

def test_remove_middle_element():
    head = create_list_from_array([1, 2, 3])
    head = remove(head, 2)
    assert list_to_array(head) == [1, 3]