N, M = map(int, input().split())
edges = {}
for i in range(1, N+1):
    edges[i] = []
for _ in range(M):
    x, y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)


def dfs(prev, i):
    if seen[i]:
        return 1
    seen[i] = True
    res = 0
    for e in edges[i]:
        if prev == e:
            continue
        res += dfs(i, e)
    return res


res = 0
seen = [False for _ in range(N+1)]
for i in range(1, N+1):
    if seen[i]:
        continue
    d = dfs(None, i)
    if d == 0:
        res += 1
print(res)
