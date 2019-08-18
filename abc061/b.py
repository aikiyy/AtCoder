n, m = map(int, input().split())
edges = [list() for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

for edge in edges:
    print(len(edge))
