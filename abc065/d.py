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


N = int(input())
XY = [[i] + list(map(int, input().split()))for i in range(N)]

edges = [[] for _ in range(N)]
sorted_xy = sorted(XY, key=lambda x: x[1])
for i in range(N-1):
    a = sorted_xy[i][0]
    b = sorted_xy[i+1][0]
    cost = sorted_xy[i+1][1] - sorted_xy[i][1]
    edges[a].append((cost, b))
    edges[b].append((cost, a))
sorted_xy = sorted(XY, key=lambda x: x[2])
for i in range(N-1):
    a = sorted_xy[i][0]
    b = sorted_xy[i+1][0]
    cost = sorted_xy[i+1][2] - sorted_xy[i][2]
    edges[a].append((cost, b))
    edges[b].append((cost, a))
ans = prim(N, 0, edges)
print(ans)
