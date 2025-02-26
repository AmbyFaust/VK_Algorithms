import pytest


def two_sum(arr: list, target: int) -> tuple[int, int]:
    l, r = 0, len(arr) - 1
    while l < r:
        tmp_summ = arr[l] + arr[r]
        if tmp_summ == target:
            return l, r
        elif tmp_summ > target:
            r -= 1
        else:
            l += 1
    return -1, -1


# Тесты
def test_two_sum_basic():
    arr = [2, 7, 11, 15]
    target = 9
    assert two_sum(arr, target) == (0, 1)

def test_two_sum_multiple_pairs():
    arr = [1, 2, 3, 4, 5]
    target = 5
    assert two_sum(arr, target) == (0, 3)

def test_two_sum_negative_numbers():
    arr = [-5, -3, 0, 1, 4]
    target = -2
    assert two_sum(arr, target) == (1, 3)

def test_two_sum_single_pair():
    arr = [1, 3, 4, 6]
    target = 7
    assert two_sum(arr, target) == (0, 3)

def test_two_sum_no_solution():
    arr = [1, 2, 3, 4]
    target = 10
    assert two_sum(arr, target) == (-1, -1)

def test_two_sum_large_array():
    arr = list(range(1, 10001))
    target = 19999
    assert two_sum(arr, target) == (9998, 9999)

def test_two_sum_duplicate_numbers():
    arr = [1, 2, 2, 3, 4]
    target = 4
    assert two_sum(arr, target) == (0, 3)

def test_two_sum_zero_target():
    arr = [-4, -3, -2, 0, 2, 5]
    target = 0
    assert two_sum(arr, target) == (2, 4)

