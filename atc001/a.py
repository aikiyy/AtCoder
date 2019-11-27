import sys
sys.setrecursionlimit(pow(10, 7))


H, W = map(int, input().split())
seen = [[False]*W for _ in range(H)]
C = []
for _ in range(H):
    C.append(input())

s, g = [0, 0], [0, 0]
for i in range(H):
    for j in range(W):
        if C[i][j] == 's':
            s = [i, j]
        if C[i][j] == 'g':
            g = [i, j]


def dfs(now):
    i, j = now
    if i < 0 or j < 0 or i >= H or j >= W:
        return
    if C[i][j] == '#' or seen[i][j]:
        return
    seen[i][j] = True
    dfs([i-1, j])
    dfs([i, j-1])
    dfs([i+1, j])
    dfs([i, j+1])


dfs(s)
print('Yes' if seen[g[0]][g[1]] else 'No')
