def k_min_node(root, k):
    stack = [None]
    cur = root
    count = 0
    while cur:
        if count == k:
            return cur.val
        if cur.left is not None:
            stack.append(cur)
            cur = cur.left
            count += 1
        elif cur.right is not None:
            stack.append(cur)
            cur = cur.right
            count += 1
        else:
            while cur.right is None:
                cur = stack.pop(-1)
            stack.append(cur)
            cur = cur.right
            count += 1
    return -1

