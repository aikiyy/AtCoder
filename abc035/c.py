n, q = map(int, input().split())

imos = [0] * (n+1)
for _ in range(q):
    l, r = map(int, input().split())
    imos[l-1] += 1
    imos[r] -= 1

for i in range(n):
    imos[i+1] += imos[i]

print(''.join(map(lambda x: str(x%2), imos[:-1])))
