import heapq


N = int(input())
A = list(map(int, input().split()))

fa = A[:N]
max_l = [0] * (N + 1)
s = sum(fa)
max_l[0] = s
heapq.heapify(fa)
for i, a in enumerate(A[N:2*N]):
    if a > fa[0]:
        s -= heapq.heappop(fa)
        s += a
        heapq.heappush(fa, a)
    max_l[i+1] = s

la = [-i for i in A[2*N:]]
min_r = [0] * (N + 1)
s = sum(la)
min_r[N] = s
heapq.heapify(la)
for i, a in enumerate(reversed(A[N:2*N])):
    if a < -la[0]:
        s -= heapq.heappop(la)
        s += -a
        heapq.heappush(la, -a)
    min_r[N-i-1] = s

print(max([l + r for l, r in zip(max_l, min_r)]))
