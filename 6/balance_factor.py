def dfs(node):
    if node is None:
        return 0

    lvl_l = dfs(node.left)
    lvl_r = dfs(node.right)
    node.b_factor = lvl_l - lvl_r
    return max(lvl_l, lvl_r) + 1


def balance_factor(root):
    dfs(root)

