h, w = map(int, input().split())
S = ['.'+input()+'.' for _ in range(h)]
S = ['.'*(w+2)] + S + ['.'*(w+2)]
flag = False
for i in range(1, h+1):
    for j in range(1, w+1):
        if S[i][j] == '.':
            continue
        if S[i-1][j] != '#' and S[i][j-1] != '#' and S[i][j+1] != '#' and S[i+1][j] != '#':
            flag = True
print('No' if flag else 'Yes')
