from linked_list import LinkedList
import pytest

def is_circle(head: LinkedList) -> bool:
    first_node = head
    second_node = head
    while first_node:
        first_node = first_node.next
        if second_node.next is None:
            return False
        elif second_node.next.next is None:
            return False
        else:
            second_node = second_node.next.next
        if first_node == second_node:
            return True
    return False


def create_linear_list():
    head = LinkedList(1)
    head.add(2)
    head.next.add(3)
    head.next.next.add(4)
    head.next.next.next.add(5)
    return head

def create_circular_list():
    head = LinkedList(1)
    head.add(2)
    head.next.add(3)
    head.next.next.add(4)
    head.next.next.next.add(5)
    head.next.next.next.next.next = head.next
    return head

def test_linear_list():
    head = create_linear_list()
    assert is_circle(head) == False

def test_circular_list():
    head = create_circular_list()
    assert is_circle(head) == True

def test_empty_list():
    head = None
    assert is_circle(head) == False

def test_single_element_list():
    head = LinkedList(1)
    assert is_circle(head) == False

def test_single_element_circular_list():
    head = LinkedList(1)
    head.next = head
    assert is_circle(head) == True

def test_two_circular_element():
    head = LinkedList(1)
    head.add(2)
    head.next.next = head
    assert is_circle(head) == True