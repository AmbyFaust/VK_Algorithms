import pytest


def list_swap(arr: list, l: int, r: int) -> None:
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

def part_list_swap(arr: list, k: int) -> None:
    if not arr:
        return
    k = k % len(arr)
    arr.reverse()
    list_swap(arr, 0, k-1)
    list_swap(arr, k, len(arr)-1)


# Тесты
def test_part_list_swap_basic():
    arr = [1, 2, 3, 4, 5, 6, 7]
    part_list_swap(arr, 3)
    assert arr == [5, 6, 7, 1, 2, 3, 4]

def test_part_list_swap_k_zero():
    arr = [1, 2, 3, 4, 5, 6, 7]
    part_list_swap(arr, 0)
    assert arr == [1, 2, 3, 4, 5, 6, 7]

def test_part_list_swap_k_greater_than_length():
    arr = [1, 2, 3, 4, 5, 6, 7]
    part_list_swap(arr, 10)
    assert arr == [5, 6, 7, 1, 2, 3, 4]

def test_part_list_swap_single_element():
    arr = [42]
    part_list_swap(arr, 1)
    assert arr == [42]

def test_part_list_swap_empty_list():
    arr = []
    part_list_swap(arr, 3)
    assert arr == []

def test_part_list_swap_negative_numbers():
    arr = [-1, -2, -3, -4, -5]
    part_list_swap(arr, 2)
    assert arr == [-4, -5, -1, -2, -3]

def test_part_list_swap_mixed_numbers():
    arr = [5, -3, 0, 2, -1]
    part_list_swap(arr, 3)
    assert arr == [0, 2, -1, 5, -3]

def test_part_list_swap_large_array():
    arr = list(range(1, 10001))
    expected = list(range(9998, 10001)) + list(range(1, 9998))
    part_list_swap(arr, 3)
    assert arr == expected
