h, w = map(int, input().split())
S = []
S.append('.' * (w + 2))
for _ in range(h):
    S.append('.' + input() + '.')
S.append('.' * (w + 2))
for i in range(1, h+1):
    l = []
    for j in range(1, w+1):
        if S[i][j] == '#':
            l.append('#')
            continue
        _s = S[i-1][j-1:j+2] + S[i][j-1] + S[i][j+1] + S[i+1][j-1:j+2]
        l.append(_s.count('#'))
    print(''.join(map(str, l)))

