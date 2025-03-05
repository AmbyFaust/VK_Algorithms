def is_b_based_on_a(a: str, b: str) -> bool:
    a_ind, b_ind = 0, 0
    if not a:
        return True
    if not b:
        return False
    while b_ind != len(b):
        if a[a_ind] == b[b_ind]:
            a_ind += 1
            if a_ind == len(a):
                return True
        b_ind += 1
    return False


def test_empty_strings():
    assert is_b_based_on_a("", "") == True

def test_b_empty_a_not_empty():
    assert is_b_based_on_a("abc", "") == False

def test_a_empty_b_not_empty():
    assert is_b_based_on_a("", "abc") == True

def test_a_and_b():
    assert is_b_based_on_a("abc", "ahsgdfbfsdfgsdfcsdfsdgfsdg") == True

def test_b_is_permutation_of_a():
    assert is_b_based_on_a("abc", "cba") == False

def test_b_missing_characters_from_a():
    assert is_b_based_on_a("abc", "ab") == False

def test_b_has_fewer_characters_than_a():
    assert is_b_based_on_a("abc", "a") == False

def test_b_is_mixed_with_extra_characters():
    assert is_b_based_on_a("abc", "cbad") == False

def test_b_has_duplicate_characters_from_a():
    assert is_b_based_on_a("abc", "aabbcc") == True