N = int(input())
S = input()

ans = 0
for i in range(0, 1000):
    num = str(i).zfill(3)
    flag = True
    _idx = 0
    for s in num:
        idx = S[_idx:].find(s)
        if idx == -1:
            flag = False
            break
        else:
            _idx += idx + 1
    if flag:
        ans += 1
print(ans)
