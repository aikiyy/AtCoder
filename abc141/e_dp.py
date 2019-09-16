N = int(input())
S = input()

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if S[i] == S[j]:
            dp[i][j] = dp[i+1][j+1]+1

ans = 0
for i in range(N):
    for j in range(i+1, N):
        now = min(dp[i][j], j-i)
        ans = max(ans, now)
print(ans)
