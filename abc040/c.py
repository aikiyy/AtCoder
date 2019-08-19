n = int(input())
a = list(map(int, input().split()))
dp = [10000] * (n+1)
dp[1] = 0
dp[2] = abs(a[1] - a[0])
for i in range(3, n+1):
    dp[i] = min(dp[i-1] + abs(a[i-1] - a[i-2]), dp[i-2] + abs(a[i-1] - a[i-3]))
print(dp[n])