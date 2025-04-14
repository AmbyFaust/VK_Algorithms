from is_same_tree import is_same_tree


def is_sub_tree(a, b):
    if a is None:
        return False
    elif b is None:
        return True
    elif is_same_tree(a, b):
        return True
    return is_sub_tree(a.left, b) or is_sub_tree(a.right, b)
