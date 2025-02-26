def niderland_flag(arr: list) -> None:
    l, i, r = 0, 0, len(arr) - 1
    while i < r:
        if arr[i] == 2:
            arr[i], arr[r] = arr[r], arr[i]
            r -= 1
        elif arr[i] == 0:
            arr[i], arr[l] = arr[l], arr[i]
            l += 1
            if l > i:
                i += 1
        else:
            i += 1


# Тесты
def test_niderland_flag_basic():
    arr = [2, 0, 2, 1, 1, 0]
    niderland_flag(arr)
    assert arr == [0, 0, 1, 1, 2, 2]

def test_niderland_flag_all_zeros():
    arr = [0, 0, 0, 0]
    niderland_flag(arr)
    assert arr == [0, 0, 0, 0]

def test_niderland_flag_all_ones():
    arr = [1, 1, 1, 1]
    niderland_flag(arr)
    assert arr == [1, 1, 1, 1]

def test_niderland_flag_all_twos():
    arr = [2, 2, 2, 2]
    niderland_flag(arr)
    assert arr == [2, 2, 2, 2]

def test_niderland_flag_mixed():
    arr = [1, 0, 2, 1, 0, 2, 1]
    niderland_flag(arr)
    assert arr == [0, 0, 1, 1, 1, 2, 2]

def test_niderland_flag_empty_list():
    arr = []
    niderland_flag(arr)
    assert arr == []

def test_niderland_flag_single_element():
    arr = [1]
    niderland_flag(arr)
    assert arr == [1]

def test_niderland_flag_already_sorted():
    arr = [0, 0, 1, 1, 2, 2]
    niderland_flag(arr)
    assert arr == [0, 0, 1, 1, 2, 2]

def test_niderland_flag_reverse_sorted():
    arr = [2, 2, 1, 1, 0, 0]
    niderland_flag(arr)
    assert arr == [0, 0, 1, 1, 2, 2]

arr = [2, 0, 2, 1, 1, 0]
niderland_flag(arr)
print(arr)