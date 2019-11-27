N, M = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    edges[x-1].append(y-1)

ans = 0
for i in range(1 << N):
    num = list(reversed(list(map(int, format(i, '0'+str(N)+'b')))))
    count = 0
    need_count = sum(range(sum(num)))
    for n in range(N):
        if i & (1 << n):
            count += len([j for j in edges[n] if num[j] == 1])
    if count == need_count:
        ans = max(ans, sum(num))
print(ans)
