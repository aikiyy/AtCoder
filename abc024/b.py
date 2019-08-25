N, T = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = 0
for i in range(N-1):
    ans += min(A[i+1]-A[i], T)
ans += T
print(ans)