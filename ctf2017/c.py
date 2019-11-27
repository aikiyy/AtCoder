from heapq import heappush, heappop


N, K = map(int, input().split())
B = []
hq = []
for i in range(N):
    a, b = map(int, input().split())
    heappush(hq, (a, i))
    B.append(b)

num = 0
ans = 0
while num < K:
    a, i = heappop(hq)
    num += 1
    ans += a
    heappush(hq, (a + B[i], i))
print(ans)
