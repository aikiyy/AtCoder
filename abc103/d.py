N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
AB = sorted(AB, key=lambda x: x[1])

ans = 0
m = 0
for ab in AB:
    if not ab[0] < m <= ab[1]:
        m = ab[1]
        ans += 1
print(ans)
