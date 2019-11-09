N, D = map(int, input().split())

num2 = 0
num3 = 0
num5 = 0
while D % 2 == 0:
    num2 += 1
    D //= 2
while D % 3 == 0:
    num3 += 1
    D //= 3
while D % 5 == 0:
    num5 += 1
    D //= 5

if D != 1:
    print(0)
    exit()

dp = [[[[0.] * (num5+1) for _ in range(num3+1)] for _ in range(num2+1)] for _ in range(N+1)]
dp[0][0][0][0] = 1.0

for n in range(N):
    for j in range(num2+1):
        for k in range(num3+1):
            for l in range(num5+1):
                dp[n+1][j][k][l] += dp[n][j][k][l] / 6
                dp[n+1][min(j+1, num2)][k][l] += dp[n][j][k][l] / 6
                dp[n+1][j][min(k+1, num3)][l] += dp[n][j][k][l] / 6
                dp[n+1][min(j+2, num2)][k][l] += dp[n][j][k][l] / 6
                dp[n+1][j][k][min(l+1, num5)] += dp[n][j][k][l] / 6
                dp[n+1][min(j+1, num2)][min(k+1, num3)][l] += dp[n][j][k][l] / 6
print(dp[N][num2][num3][num5])
