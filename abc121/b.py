# -*- coding: utf-8 -*-


N, M, C = map(int, input().split(' '))
B = list(map(int, input().split(' ')))
ans = 0
for _ in range(N):
    a = list(map(int, input().split(' ')))
    if sum([x * y for x, y in zip(a, B)]) + C > 0:
        ans += 1
print(ans)