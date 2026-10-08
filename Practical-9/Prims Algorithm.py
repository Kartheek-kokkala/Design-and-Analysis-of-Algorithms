
graph = [
    [0, 2, 3, 0],
    [2, 0, 1, 4],
    [3, 1, 0, 5],
    [0, 4, 5, 0]
]

n = len(graph)
visited = [False] * n
visited[0] = True

print("Edges in Minimum Spanning Tree:")

for _ in range(n - 1):
    min_weight = float('inf')
    x = y = 0

    for i in range(n):
        if visited[i]:
            for j in range(n):
                if not visited[j] and graph[i][j] != 0:
                    if graph[i][j] < min_weight:
                        min_weight = graph[i][j]
                        x = i
                        y = j

    print(x, "-", y, ":", min_weight)
    visited[y] = True
