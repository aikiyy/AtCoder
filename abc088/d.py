from collections import deque

H, W = map(int, input().split())
S = ['#'*(W+2)]
white_num = 0
for _ in range(H):
    s = input()
    white_num += s.count('.')
    S.append('#'+s+'#')
S.append('#'*(W+2))

C = [[-1]*(W+2) for _ in range(H+2)]
C[1][1] = 1
q = deque()
q.append((1, 1))
xlist = [0, 0, 1, -1]
ylist = [1, -1, 0, 0]
while len(q) > 0:
    x, y = q.popleft()
    for i in range(4):
        mx = x + xlist[i]
        my = y + ylist[i]
        if S[mx][my] == '#' or C[mx][my] >= 0:
            continue
        C[mx][my] = C[x][y] + 1
        q.append((mx, my))
if C[H][W] == -1:
    print(-1)
else:
    print(white_num - C[H][W])
