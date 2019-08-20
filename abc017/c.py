n, m = map(int, input().split())
imos = [0] * (m+1)
total = 0
for _ in range(n):
    l, r, s = map(int, input().split())
    imos[l-1] += s
    imos[r] -= s
    total += s
for i in range(m):
    imos[i+1] += imos[i]
print(total - min(imos[:-1]))