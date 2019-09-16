N, K, Q = map(int, input().split())

A = [-Q + K] * N
for _ in range(Q):
    A[int(input()) - 1] += 1

for a in A:
    if a > 0:
        print('Yes')
    else:
        print('No')
