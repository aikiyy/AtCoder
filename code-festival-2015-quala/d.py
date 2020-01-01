N, M = map(int, input().split())
X = [int(input())-1 for _ in range(M)]


def calc(t):
    # Mi人目が何両目までチェックできるか
    d = [0] * M
    l = X[0]
    d[0] = X[0] + max(t - l * 2, (t - l) // 2)
    for i in range(1, M):
        if d[i-1] < X[i] - t - 1:
            return False
        l = max(X[i] - d[i-1] - 1, 0)
        if i == M-1:
            d[i] = X[i] + max(t - l * 2, (t - l) // 2)
        else:
            d[i] = min(X[i] + max(t - l * 2, (t - l) // 2), X[i+1])
    if d[M-1] >= N:
        return True
    else:
        return False


l = 0
r = N
_mid = 0
while r - l > 1:
    mid = (l + r) // 2
    if calc(mid):
        r = mid
    else:
        l = mid
print(r)
