def null_to_end(arr: list) -> None:
    l, i = 0, 0
    while i < len(arr):
        if arr[i] != 0:
            arr[i], arr[l] = arr[l], arr[i]
            l += 1
        i += 1

# Тесты
def test_null_to_end_basic():
    arr = [0, 33, 57, 88, 60, 0, 0, 80, 99]
    null_to_end(arr)
    assert arr == [33, 57, 88, 60, 80, 99, 0, 0, 0]

def test_null_to_end_all_zeros():
    arr = [0, 0, 0, 0]
    null_to_end(arr)
    assert arr == [0, 0, 0, 0]

def test_null_to_end_no_zeros():
    arr = [33, 57, 88, 60, 80, 99]
    null_to_end(arr)
    assert arr == [33, 57, 88, 60, 80, 99]

def test_null_to_end_empty_list():
    arr = []
    null_to_end(arr)
    assert arr == []

def test_null_to_end_single_zero():
    arr = [0]
    null_to_end(arr)
    assert arr == [0]

def test_null_to_end_single_non_zero():
    arr = [99]
    null_to_end(arr)
    assert arr == [99]

def test_null_to_end_zeros_at_end():
    arr = [33, 57, 88, 60, 80, 99, 0, 0, 0]
    null_to_end(arr)
    assert arr == [33, 57, 88, 60, 80, 99, 0, 0, 0]

def test_null_to_end_zeros_at_start():
    arr = [0, 0, 0, 33, 57, 88, 60, 80, 99]
    null_to_end(arr)
    assert arr == [33, 57, 88, 60, 80, 99, 0, 0, 0]
