D, N = map(int, input().split())
T = [int(input()) for _ in range(D)]
ABC = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j]: i日目に服jを選ぶときの派手さの差の最大合計値
dp = [[-1e10 for _ in range(N+1)]for _ in range(D+1)]

# 1日目
for i, (a, b, c) in enumerate(ABC):
    if a <= T[0] <= b:
        dp[0][i] = 0

for i in range(1, D):
    for j in range(N):
        if ABC[j][0] <= T[i] <= ABC[j][1]:
            dp[i][j] = max([dp[i-1][jj] + abs(ABC[jj][2] - ABC[j][2]) for jj in range(N)])

print(max(dp[D-1]))
