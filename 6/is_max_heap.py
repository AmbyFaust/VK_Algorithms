def is_max_heap(arr):
    for i in range(len(arr)):
        l = 2 * i + 1
        r = 2 * i + 2
        if l < len(arr) and arr[l] > arr[i]:
            return False
        if r < len(arr) and arr[r] > arr[i]:
            return False
    return True

print(is_max_heap([1]))