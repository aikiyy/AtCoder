N = int(input())
H = list(map(int, input().split()))
ans = 0
_ans = 0
for i in range(1, N):
    if H[i-1] >= H[i]:
        _ans += 1
    else:
        _ans = 0
    ans = max(ans, _ans)
print(ans)
