
edges = [
    (2, 0, 1),
    (3, 0, 2),
    (1, 1, 2),
    (4, 1, 3),
    (5, 2, 3)
]


edges.sort()

parent = [0, 1, 2, 3]

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        return True
    return False

print("Edges in Minimum Spanning Tree:")
