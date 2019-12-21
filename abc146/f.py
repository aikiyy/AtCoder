N, M = map(int, input().split())
S = input()
S = list(reversed(S))

# 現在位置
now = 0
_now = 0
ans = []
while now <= N-1:
    for i in range(min(M, N-now), 0, -1):
        if S[now+i] == '0':
            ans.append(i)
            now += i
            break
    if _now == now:
        print(-1)
        exit()
    _now = now
print(*reversed(ans))
