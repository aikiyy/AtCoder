N, K = map(int, input().split())
A = list(map(int, input().split()))
_ans = sum(A[:K])
ans = _ans
for i in range(K, N):
    _ans = _ans + A[i] - A[i-K]
    ans += _ans
print(ans)
