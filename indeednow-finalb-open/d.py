import heapq


def prim(n, s, edges):
    # n:頂点数, s:スタートノード
    # edges: edgeリスト(cost, 行き先ノード)
    used = [False] * n
    edgelist = []
    for e in edges[s]:
        heapq.heappush(edgelist, e)
    used[s] = True
    res = 0
    while len(edgelist) != 0:
        minedge = heapq.heappop(edgelist)
        if used[minedge[1]]:
            continue
        used[minedge[1]] = True
        for e in edges[minedge[1]]:
            if not used[e[1]]:
                heapq.heappush(edgelist, e)
        res += minedge[0]
    return res


H, W = map(int, input().split())
S = list(map(int, input().split()))
G = list(map(int, input().split()))
P = [list(map(int, input().split())) for _ in range(H)]

edges = [[] for _ in range(H*W)]
# 高さ
for h in range(H):
    # 幅
    for w in range(W):
        # 上
        if h-1 >= 0:
            cost = P[h-1][w] * P[h][w]
            edges[w+W*h].append((-cost, w+W*(h-1)))
        # 右
        if w+1 < W:
            cost = P[h][w+1] * P[h][w]
            edges[w+W*h].append((-cost, w+1+W*h))
        # 左
        if w-1 >= 0:
            cost = P[h][w-1] * P[h][w]
            edges[w+W*h].append((-cost, w-1+W*h))
        # 下
        if h+1 < H:
            cost = P[h+1][w] * P[h][w]
            edges[w+W*h].append((-cost, w+W*(h+1)))

s = S[0]+W*(S[1]-1)-1
print(s)
total_p = sum([sum(p) for p in P])
ans = prim(H*W, s, edges) - total_p
print(-ans)
