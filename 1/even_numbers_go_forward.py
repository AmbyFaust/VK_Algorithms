def go_forward(arr: list) -> None:
    l, i = 0, 0
    while i < len(arr):
        if arr[i] % 2 == arr[l] % 2:
            if arr[i] % 2 == 0:
                l += 1
            i += 1
        else:
            if arr[i] % 2 == 0:
                arr[i], arr[l] = arr[l], arr[i]
                l += 1
            i += 1

# Тесты
def test_go_forward_basic():
    arr = [3, 1, 2, 4, 6, 5]
    go_forward(arr)
    assert arr[:3] == [2, 4, 6] and [el % 2 for el in arr[3:]] == [1,1,1]

def test_go_forward_all_even():
    arr = [2, 4, 6, 8]
    go_forward(arr)
    assert arr == [2, 4, 6, 8]

def test_go_forward_all_odd():
    arr = [1, 3, 5, 7]
    go_forward(arr)
    assert arr == [1, 3, 5, 7]

def test_go_forward_empty_list():
    arr = []
    go_forward(arr)
    assert arr == []

def test_go_forward_single_element():
    arr = [2]
    go_forward(arr)
    assert arr == [2]

def test_go_forward_negative_numbers():
    arr = [-1, -2, -3, -4, -5]
    go_forward(arr)
    assert arr[:2] == [-2, -4] and [el % 2 for el in arr[2:]] == [1, 1, 1]

def test_go_forward_preserve_order():
    arr = [5, 4, 3, 2, 6, 1]
    go_forward(arr)
    assert arr == [4, 2, 6, 5, 3, 1]
