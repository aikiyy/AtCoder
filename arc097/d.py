N, M = map(int, input().split())
P = list(map(int, input().split()))

root = list(range(1, N+1))


def find(x):
    if root[x-1] == x:
        return x
    else:
        root[x-1] = find(root[x-1])
        return root[x-1]


for _ in range(M):
    x, y = map(int, input().split())
    x = find(x)
    y = find(y)
    root[max(x, y) - 1] = min(x, y)

ans = 0
for i in range(1, N+1):
    if find(i) == find(P[i-1]):
        ans += 1
print(ans)
