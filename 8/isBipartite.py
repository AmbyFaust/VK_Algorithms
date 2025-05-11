def isBipartite(graph):
    colors = [0] * len(graph)

    def dfs(v, c):
        colors[v] = c
        for el in graph[v]:
            if colors[el] == 0:
                if not dfs(el, -c):
                    return False
            elif colors[el] == colors[v]:
                return False
        return True

    for i in range(len(graph)):
        if colors[i] == 0:
            if not dfs(i, 1):
                return False
    return True