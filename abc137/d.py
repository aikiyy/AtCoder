import numpy as np


n, m = map(int, input().split(' '))
ab = []
for _ in range(n):
    ab.append(list(map(int, input().split(' '))))
# print(sorted(ab, key=lambda x: (-x[1], -x[0])))

ans = 0
while m > 0:
    _ab = list(filter(lambda x: x[0] <= m, ab))
    if len(_ab) == 0:
        break
    revenue = max(list(map(lambda x: x[1], _ab)))
    delete_ab = sorted(list(filter(lambda x: x[1] == revenue, ab)), reverse=True)[0]
    ab.remove(delete_ab)
    ans += delete_ab[1]
    m -= 1
print(ans)
