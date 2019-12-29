import sys
sys.setrecursionlimit(pow(10, 7))


# vをcに塗る。pはvの親
def dfs(v, p, c):
    res[v] = c
    for e in G[v]:
        if e[0] == p:
            continue
        if e[1] & 1:
            dfs(e[0], v, 1-c)
        else:
            dfs(e[0], v, c)


N = int(input())

G = [[] for _ in range(N)]
res = [0] * N
for _ in range(N-1):
    u, v, w = map(int, input().split())
    G[u-1].append([v-1, w])
    G[v-1].append([u-1, w])
dfs(0, -1, 1)
print('\n'.join(map(str, res)))
