import sys
sys.setrecursionlimit(pow(10, 7)) 


# 頂点vをcolor(1 or -1)で塗り、矛盾がないか調べる
def dfs(v, color):
    colors[v] = color
    for to in edges[v]:
        # 同じ色が隣接するならFalse
        if colors[to] == color:
            return False
        # 未着手の頂点は反転した色を指定
        if colors[to] == 0 and not dfs(to, -color):
            return False
    return True


N, M = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
colors = [0] * N
if dfs(0, 1):
    print(len([i for i in colors if i == -1])*len([j for j in colors if j == 1]) - M)
else:
    print(N * (N-1) // 2 - M)
