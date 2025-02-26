import pytest

def all_sum(arr: list) -> int:
    if len(arr) == 0:
        return 0
    if len(arr) % 2 == 0:
        return (arr[0] + arr[-1]) * (len(arr) // 2)
    else:
        return (arr[0] + arr[-1]) * (len(arr) // 2) + arr[len(arr)//2]

# Тесты
def test_all_sum_even_length():
    arr = [1, 2, 3, 4]
    assert all_sum(arr) == 10

def test_all_sum_odd_length():
    arr = [1, 2, 3, 4, 5]
    assert all_sum(arr) == 15

def test_all_sum_single_element():

    arr = [7]
    assert all_sum(arr) == 7

def test_all_sum_empty_list():
    arr = []
    assert all_sum(arr) == 0

def test_all_sum_large_list():
    arr = list(range(1, 1000001))
    expected_sum = 1000000 * (1000000 + 1) // 2
    assert all_sum(arr) == expected_sum

def test_all_sum_negative_numbers():
    arr = [-3, -2, -1, 0, 1, 2, 3]
    assert all_sum(arr) == 0
