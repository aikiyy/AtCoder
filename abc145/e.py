N, T = map(int, input().split())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

max_len = T + 1
dp = [[0 for _ in range(max_len)]for _ in range(N+1)]

ans = 0
for i in range(N):
    for j in range(max_len):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if j < T:
            if j + A[i] > T:
                ans = max(ans, dp[i][j]+B[i])
            else:
                dp[i+1][j+A[i]] = max(dp[i+1][j+A[i]], dp[i][j] + B[i])
print(max(dp[N][T], ans))
