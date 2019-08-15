n, m = map(int, input().split())
edges = [set() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a-1].add(b-1)
    edges[b-1].add(a-1)

for i in range(n):
    print(len({n for v in edges[i] for n in edges[v] if not n in edges[i] and n != i}))
