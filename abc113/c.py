import collections
import bisect


N, M = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(M)]
a = collections.defaultdict(list)
for x, y in sorted(P):
    a[x] += [y]
for x, y in P:
    idx = bisect.bisect(a[x], y)
    print(str(x).zfill(6), str(idx).zfill(6), sep='')
