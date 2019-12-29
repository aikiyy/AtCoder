def bellman_ford(edges, n, src):
    # n:ノード数, src:スタートノード
    # edges:edge(src, tgt, cost)のリスト
    inf = float('inf')
    dist = [inf for _ in range(n)]
    dist[src] = 0
    # 移動経路
    pre = {}

    # 最短経路算出
    for i in range(n-1):
        for edge in edges:
            # srcにコストがあり、tgtのコストよりも低いコストで更新できそうなら
            if dist[edge[0]] != inf and dist[edge[1]] > dist[edge[0]] + edge[2]:
                dist[edge[1]] = dist[edge[0]] + edge[2]
                pre[edge[1]] = edge[0]

    # 負の閉路検出
    def checkpath(pre, n, src):
        if src in pre and pre[n-1] == src and pre[src] == n-1:
            return True
        count = 0
        p = pre[n-1]
        while p != src:
            p = pre[p]
            if p == src and src in pre:
                return True
            count += 1
            if count >= n-1:
                return True
        return False

    is_cycle = checkpath(pre, n, src)
    return (dist, is_cycle)


N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a-1, b-1, -c))

d, is_cycle = bellman_ford(edges, N, 0)
if is_cycle:
    print('inf')
else:
    print(-d[N-1])