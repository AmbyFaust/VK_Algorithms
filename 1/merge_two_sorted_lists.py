def merge_two_sorted_lists(arr1: list, arr2: list) -> list:
    r1, r2, r = len(arr1) - 1, len(arr2) - 1, len(arr1) + len(arr2) - 1
    for i in range(r1 + 1, r + 1):
        arr1.append(0)
    while r > -1:
        if r1 < 0:
            for i in range(r2, -1, -1):
                arr1[r] = arr2[i]
                r -= 1
        if r2 < 0:
            for i in range(r1, -1, -1):
                arr1[r] = arr1[i]
                r -= 1
        if arr1[r1] < arr2[r2]:
            arr1[r] = arr2[r2]
            r2 -= 1
        else:
            arr1[r] = arr1[r1]
            r1 -= 1
        r -= 1
    return arr1

#Тесты
def test_merge_two_sorted_lists_basic():
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    assert merge_two_sorted_lists(arr1, arr2) == [1, 2, 3, 4, 5, 6]

def test_merge_two_sorted_lists_one_empty():
    arr1 = []
    arr2 = [1, 2, 3]
    assert merge_two_sorted_lists(arr1, arr2) == [1, 2, 3]

def test_merge_two_sorted_lists_both_empty():
    arr1 = []
    arr2 = []
    assert merge_two_sorted_lists(arr1, arr2) == []

def test_merge_two_sorted_lists_duplicate_numbers():
    arr1 = [1, 2, 2, 3]
    arr2 = [2, 4, 5]
    assert merge_two_sorted_lists(arr1, arr2) == [1, 2, 2, 2, 3, 4, 5]

def test_merge_two_sorted_lists_negative_numbers():
    arr1 = [-3, -1, 0]
    arr2 = [-2, 2, 4]
    assert merge_two_sorted_lists(arr1, arr2) == [-3, -2, -1, 0, 2, 4]

def test_merge_two_sorted_lists_large_arrays():
    arr1 = list(range(1, 10001, 2))
    arr2 = list(range(2, 10001, 2))
    expected = list(range(1, 10001))
    assert merge_two_sorted_lists(arr1, arr2) == expected

