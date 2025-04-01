def copy_time(n, x, y):
    if x > y:
        x, y = y, x

    left, right = x, n * x

    while left < right:
        mid = (left + right) // 2

        if (mid // x) + (mid // y) >= n + 1:
            right = mid
        else:
            left = mid + 1

    return left