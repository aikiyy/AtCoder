from heapq import heappush, heappop


N, M = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

same_num = []
for a in A:
    heappush(same_num, -2 * a)
diff_num = []
for i in range(N):
    for j in range(i+1, N):
        heappush(diff_num, -A[i] - A[j])

while True:
    s = -1 * heappop(same_num)
    d = -1 * heappop(diff_num)
    if s > d:
        ans += s
        M -= 1
        heappush(diff_num, -d)
    else:
        ans += 2 * d
        M -= 2
        heappush(same_num, -s)
    if M <= 0:
        break
if M == -1:
    ans -= d
print(ans)
