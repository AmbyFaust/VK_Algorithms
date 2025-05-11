def isTree(graph, start):
    visited = []
    queue = [start]
    parent = {start: None}
    while queue:
        vertex = queue.pop(0)
        visited.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                parent[neighbor] = vertex
            else:
                if parent[vertex] == neighbor:
                    return False

    return len(visited) == len(graph)