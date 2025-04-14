def is_symmetric(root):
    if root is None:
        return True
    queue = [root]
    while queue:
        qlen = len(queue)
        for i in range(qlen):
            if queue[i] is None and queue[qlen - 1 - i] is None:
                continue
            elif queue[i] is None or queue[qlen - 1 - i] is None:
                return False
            elif queue[i].val != queue[qlen - 1 - i].val:
                return False

            queue.append(queue[i].left)
            queue.append(queue[i].right)
        queue = queue[qlen:]
    return True

