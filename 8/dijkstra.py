import heapq


def dijkstra(graph, start):
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    p_queue = [(0, start)]
    while p_queue:
        cur_dist, cur_v = heapq.heappop(p_queue)
        if cur_dist > dist[cur_v]:
            continue
        for neighbor, weight in graph[cur_v].items():
            next_dist = cur_dist + weight
            if next_dist < dist[neighbor]:
                dist[neighbor] = next_dist
                heapq.heappush(p_queue, (next_dist, neighbor))
    return dist