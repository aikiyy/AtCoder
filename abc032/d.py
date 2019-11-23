N, W = map(int, input().split())
V = []
W = []
for _ in range(N):
    v, w = map(intk input().split())
    V.append(v)
    W.append(w)

max_v = max(V)
max_w = max(W)
sum_v = sum(V)
sum_w = sum(W)

if sum_w <= W:
    ans = sum_v
elif N <= 30: # branch and bound

VW = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(W+1):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if j + VW[i][1] <= W:
            dp[i+1][j + VW[i][1]] = max(dp[i+1][j+VW[i][1]], dp[i][j] + VW[i][0])
print(dp[N][W])
