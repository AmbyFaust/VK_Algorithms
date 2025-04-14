def dfs(a, b):
    if a is None or b is None:
        return 0
    count = 0
    if a.val == b.val:
        count += 1

    count += dfs(a.left, b.right) + dfs(a.right, b.left)
    return count

def count_mirrors(root):
    if root is None:
        return 0
    return dfs(root.left, root.right)