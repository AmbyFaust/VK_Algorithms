def find_con_components(graph):
    visited = [None] * len(graph)
    def dfs(p, color):
        visited[p] = color
        for el in graph[p]:
            if visited[el] is None:
                dfs(el, color)
    b_color = 0
    for i in range(len(graph)):
        if visited[i] is None:
            dfs(i, b_color)
            b_color += 1

    return visited


# graph = [
#     [1,2],
#     [0,2],
#     [0,1],
#     [4],
#     [3,5],
#     [4,6],
#     [5,7],
#     [6],
#     []
# ]



