
INF = 999

# Adjacency matrix
graph = [
    [0, 4, INF],
    [INF, 0, 2],
    [3, INF, 0]
]

n = len(graph)

# Floyd-Warshall Algorithm
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(
                graph[i][j],
                graph[i][k] + graph[k][j]
            )

# Display shortest distance matrix
print("Shortest Distance Matrix:")

for row in graph:
    print(row)
