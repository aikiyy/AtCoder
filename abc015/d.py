W = int(input())
N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j]: i枚使い、重要度jを達成するための幅合計の最小値
dp = [[10001 for _ in range(5001)] for _ in range(N+1)]
dp[0][0] = 0

total_w = 0
for i in range(N):
    a, b = AB[i]
    for x in range(i, -1, -1):
        for y in range(total_w, -1, -1):
            dp[x+1][y+b] = min(dp[x+1][y+b], dp[x][y]+a)
    total_w += b

ans = 0
for i in range(K+1):
    for j in range(5001):
        if dp[i][j] <= W:
            ans = max(ans, j)
print(ans)
