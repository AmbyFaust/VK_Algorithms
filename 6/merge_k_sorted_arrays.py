import heapq


def merge_k_sorted_arrays(sorted_arrays):
    heap = []
    for i in range(len(sorted_arrays)):
        if sorted_arrays[i]:
            heapq.heappush(heap, (sorted_arrays[i][0], i, 0))
    res = []
    while heap:
        val, k, i = heapq.heappop(heap)
        res.append(val)
        if i + 1 < len(sorted_arrays[k]):
            heapq.heappush(heap, (sorted_arrays[k][i + 1], k, i + 1))
    return res
