n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]

ans = []
for i in range(1, 1024):
    x = list(map(int, (bin(i)[2:].zfill(10))))
    _ans = 0
    for j in range(n):
        c = sum(map(lambda x, y: x*y, x, f[j]))
        _ans += p[j][c]
    ans.append(_ans)
print(max(ans))
