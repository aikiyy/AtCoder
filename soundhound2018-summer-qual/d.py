from itertools import accumulate


def dijkstra(n, s, adj_list):
    # 始点sから各頂点への最短距離
    # n: 頂点数
    from heapq import heappush, heappop

    dists = [float('inf')] * n
    dists[s] = 0
    heap, rem = [(0, s)], n - 1

    while heap and rem:
        cost, src = heappop(heap)
        if dists[src] < cost:
            continue
        rem -= 1

        for dest, _cost in adj_list[src]:
            newcost = cost + _cost
            if dists[dest] > newcost:
                dists[dest] = newcost
                heappush(heap, (newcost, dest))

    return dists


N, M, S, T = map(int, input().split())
S -= 1
T -= 1
adj_yen = [[] for _ in range(N)]
adj_snuuk = [[] for _ in range(N)]
for _ in range(M):
    u, v, a, b = map(int, input().split())
    u -= 1
    v -= 1
    adj_yen[u].append((v, a))
    adj_yen[v].append((u, a))
    adj_snuuk[u].append((v, b))
    adj_snuuk[v].append((u, b))
yen_cost = dijkstra(N, S, adj_yen)
snuuk_cost = dijkstra(N, T, adj_snuuk)
ans = list(accumulate([10**15-yen-snuuk for yen, snuuk in zip(yen_cost, snuuk_cost)][::-1], max))[::-1]
print('\n'.join(map(str, ans)))
