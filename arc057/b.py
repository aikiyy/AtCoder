import math
import bisect


N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

if sum(A) == K:
    print(1)
    exit()

# i日目までにj回機嫌が良かった日の最小勝利数
dp = [[0] + [10**10] * N for _ in range(N+1)]
dp[1][1] = 1
sum_a = A[0]
for i in range(2, N+1):
    for j in range(1, i+1):
        win = math.floor(dp[i-1][j-1]*A[i-1]/sum_a) + 1
        dp[i][j] = min(dp[i-1][j-1] + win, dp[i-1][j])
    sum_a += A[i-1]

idx = bisect.bisect_left(dp[N], K)
if dp[N][idx] == K:
    print(idx)
else:
    print(idx-1)
