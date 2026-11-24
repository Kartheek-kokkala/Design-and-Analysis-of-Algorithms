
from itertools import permutations

# Cost matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(graph)
cities = list(range(1, n))

min_cost = float('inf')
best_path = []

# Generate all possible paths
for path in permutations(cities):
    cost = 0
    k = 0

    for city in path:
        cost += graph[k][city]
        k = city

    cost += graph[k][0]

    if cost < min_cost:
        min_cost = cost
        best_path = [0] + list(path) + [0]

# Display result
print("Minimum Cost:", min_cost)
print("Best Path:", best_path)
