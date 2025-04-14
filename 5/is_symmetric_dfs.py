def dfs(root, res):
    if root is None:
        return
    dfs(root.left, res)
    res.append(root.val)
    dfs(root.right, res)


def is_symmetric(root):
    if root is None:
        return True
    data = []
    dfs(root, data)
    for i in range(len(data)):
        if data[i] != data[len(data) - i - 1]:
            return False
    return True


