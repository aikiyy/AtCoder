import bisect


N, M = map(int, input().split())
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
t = 0
while True:
    if ans%2 == 0:
        idx = bisect.bisect_left(A, t)
        if idx == N:
            break
        t = A[idx] + X
    else:
        idx = bisect.bisect_left(B, t)
        if idx == M:
            break
        t = B[idx] + Y
    ans += 1
print(ans//2)
