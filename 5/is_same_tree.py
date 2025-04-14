def is_same_tree(a, b):
    if a is None and b is None:
        return True
    elif a is None or b is None:
        return False
    elif a.val != b.val:
        return False
    return is_same_tree(a.left, b.left) and is_same_tree(a.right, b.right)
