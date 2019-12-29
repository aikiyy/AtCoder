def dijkstra(n, s, adj_list):
    # 始点sから各頂点への最短距離
    # n: 頂点数, adj_list:各頂点が(先のノード, cost)を持ったリスト
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


N, K = map(int, input().split())
adj_list = [[] for _ in range(N)]
for _ in range(K):
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        res = dijkstra(N, arr[1]-1, adj_list)
        if res[arr[2]-1] == 1e1000:
            print(-1)
        else:
            print(res[arr[2]-1])
    else:
        adj_list[arr[1]-1].append((arr[2]-1, arr[3]))
        adj_list[arr[2]-1].append((arr[1]-1, arr[3]))
