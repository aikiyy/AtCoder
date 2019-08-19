n = int(input())
ng = [int(input()) for _ in range(3)]

if n in ng:
    print('NO')
    exit()

dp = [101] * (n+3)
dp[n] = 0

for i in range(n-1, -1, -1):
    if i in ng:
        continue
    dp[i] = min(dp[i+1], dp[i+2], dp[i+3]) + 1

print('YES' if dp[0] <= 100 else 'NO')
