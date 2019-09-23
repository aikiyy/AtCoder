from collections import Counter

L, R = map(int, input().split())
l = Counter(list(input().split()))
r = Counter(list(input().split()))

ans = 0
for k in l.keys():
    ans += min(l[k], r[k])
print(ans)
