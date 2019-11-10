from collections import Counter

N = int(input())
D = list(map(int, input().split()))

if D[0] != 0:
    print(0)
    exit()

ans = 1
idx = 1
C = sorted(Counter(D[1:]).items())
for k, v in C:
    if k != idx:
        print(0)
        exit()
    if k == 1:
        _v = v
    else:
        ans = ans * _v ** v % 998244353
        _v = v
    idx += 1
print(ans)
