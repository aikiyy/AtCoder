from itertools import combinations

N = int(input())
S = [input() for _ in range(N)]

ans = 0
for s in combinations(S, 3):
    _flag = True
    pre = list(map(lambda x: x[0], s))
    for p in pre:
        if p not in ['M', 'A', 'R', 'C', 'H']:
            _flag = False
    if len(pre) != len(list(set(pre))):
        _flag = False
    if _flag:
        ans += 1
print(ans)
