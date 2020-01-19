N = int(input())
P = list(map(int, input().split()))
ans = 1
max_num = P[0]
for i in range(1, N):
    if max_num >= P[i]:
        ans += 1
        max_num = P[i]
print(ans)
