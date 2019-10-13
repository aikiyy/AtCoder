from collections import deque

H, W, N = map(int, input().split())
F = [list(input()) for _ in range(H)]
NUM = [None for _ in range(N+1)]
for i in range(H):
    for j in range(W):
        if F[i][j].isdigit():
            NUM[int(F[i][j])] = (i, j)
        if F[i][j] == 'S':
            NUM[0] = (i, j)

# 何番を目指すか
xlist = [0, 0, 1, -1]
ylist = [1, -1, 0, 0]
ans = 0
for n in range(1, N+1):
    costs = [[-1]*W for _ in range(H)]
    q = deque()
    q.append((NUM[n-1], 0))
    while len(q) >= 1:
        now, cost = q.popleft()
        if now == NUM[n]:
            break
        costs[now[0]][now[1]] = cost + 1
        for i in range(4):
            mx = now[0] + xlist[i]
            my = now[1] + ylist[i]
            if mx < 0 or my < 0 or mx >= H or my >= W or costs[mx][my] >= 0 or F[mx][my] == 'X':
                continue
            q.append(((mx, my), cost+1))
    ans += cost
print(ans)
