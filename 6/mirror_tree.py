def mirror_tree(root):
    if root is None:
        return
    mirror_tree(root.left)
    mirror_tree(root.right)
    root.left, root.right = root.right, root.left

