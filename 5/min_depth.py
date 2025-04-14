def min_depth(root):
    if root is None:
        return 0

    elif root.left is None and root.right is None:
        return 1
    elif root.left is not None and root.right is not None:
        return min(min_depth(root.left), min_depth(root.right))
    elif root.left is not None:
        return 1 + min_depth(root.left)
    elif root.right is not None:
        return 1 + min_depth(root.right)
