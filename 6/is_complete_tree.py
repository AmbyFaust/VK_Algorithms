def is_complete_tree(root):
    if root is None:
        return True
    queue = [root]
    flag = False
    while queue:
        val = queue.pop(0)
        if val is None:
            flag = True
        else:
            if flag:
                return False
            queue.append(val.left)
            queue.append(val.right)
    return True
