import math


N, M, L, X = map(int, input().split())
A = list(map(int, input().split()))

# i番目までを調べた時のjにいるための最小の周回数
dp = [[10**10] * M for _ in range(N+1)]
dp[0][0] = 1

for i in range(0, N):
    for j in range(0, M):
        dp[i+1][(j+A[i])%M] = min(dp[i][(j+A[i])%M], dp[i][j] + math.floor((j+A[i])/M))
if dp[N][L] <= X:
    print('Yes')
else:
    print('No')
