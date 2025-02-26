import pytest

def list_swap(arr: list) -> None:
    l, r = 0, len(arr) - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

# Тесты
def test_list_swap_basic():
    arr = [1, 2, 3, 4]
    list_swap(arr)
    assert arr == [4, 3, 2, 1]

def test_list_swap_empty_list():
    arr = []
    list_swap(arr)
    assert arr == []

def test_list_swap_single_element():
    arr = [42]
    list_swap(arr)
    assert arr == [42]

def test_list_swap_negative_numbers():
    arr = [-1, -2, -3, -4]
    list_swap(arr)
    assert arr == [-4, -3, -2, -1]

def test_list_swap_mixed_numbers():
    arr = [5, -3, 0, 2, -1]
    list_swap(arr)
    assert arr == [-1, 2, 0, -3, 5]

def test_list_swap_duplicate_numbers():
    arr = [1, 2, 2, 3, 3]
    list_swap(arr)
    assert arr == [3, 3, 2, 2, 1]

def test_list_swap_large_array():
    arr = list(range(1, 10001))
    expected = list(range(10000, 0, -1))
    list_swap(arr)
    assert arr == expected


