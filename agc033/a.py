H, W = map(int, input().split())
C = [[False]*W for _ in range(H)]

q = []
for i in range(H):
    S = input()
    for j, x in enumerate(S):
        if x == '.':
            continue
        q.append((i, j))
        C[i][j] = True

cnt = 0
while q:
    cnt += 1
    q2 = []
    for x, y in q:
        if x-1 >= 0 and not C[x-1][y]:
            C[x-1][y] = True
            q2.append((x-1, y))
        if x+1 < H and not C[x+1][y]:
            C[x+1][y] = True
            q2.append((x+1, y))
        if y-1 >= 0 and not C[x][y-1]:
            C[x][y-1] = True
            q2.append((x, y-1))
        if y+1 < W and not C[x][y+1]:
            C[x][y+1] = True
            q2.append((x, y+1))
    q = q2
print(cnt-1)
