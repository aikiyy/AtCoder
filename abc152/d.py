def get_pair(x):
    s = int(str(x)[0])
    e = x % 10
    return s, e


N = int(input())
freq = {}
for i in range(1, N+1):
    s, e = get_pair(i)
    freq[(s, e)] = freq.get((s, e), 0) + 1
ans = 0
for s, e in freq:
    ans += freq.get((s, e), 0) * freq.get((e, s), 0)
print(ans)
