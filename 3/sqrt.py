def binary_search_sqrt(target: int) -> int:
    if target < 0:
        return -1
    if target == 0 or target == 1:
        return target

    l = 1
    r = target
    mid = 0

    while l <= r:
        mid = (l + r) // 2
        mid_squared = mid * mid
        if mid_squared == target:
            return mid
        elif mid_squared < target:
            l = mid + 1
        else:
            r = mid - 1

    if abs(mid * mid - target) <= abs((mid + 1) * (mid + 1) - target):
        return mid
    else:
        return mid + 1