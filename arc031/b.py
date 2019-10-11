field = []
N = 10
for _ in range(N):
    field.append(input())


xlist = [-1, 0, 0, 1]
ylist = [0, 1, -1, 0]


def dfs(x, y):
    f[x] = f[x][:y] + 'x' + f[x][y+1:]
    for m in range(4):
        mx = x + xlist[m]
        my = y + ylist[m]
        if mx < 0 or my < 0 or mx > 9 or my > 9 or f[mx][my] == 'x':
            continue
        dfs(mx, my)
    return


# 埋める場所を指定
for i in range(N):
    for j in range(N):
        if field[i][j] == 'o':
            continue
        f = field.copy()
        f[i] = f[i][:j] + 'o' + f[i][j+1:]
        res = 0
        for k in range(N):
            for l in range(N):
                if f[k][l] == 'x':
                    continue
                dfs(k, l)
                res += 1
        if res == 1:
            print('YES')
            exit()
print('NO')
