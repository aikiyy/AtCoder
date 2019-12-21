N, M = map(int, input().split())
S = input()

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

# 辞書順最小化を目指す
ans = sorted(ans)
new_ans = []
now = 0
while len(ans) > 0:
    for a in ans:
        if S[now+a] == '0':
            new_ans.append(a)
            ans.remove(a)
            now += a
            break
print(*new_ans)
