# -*- coding: utf-8 -*-


N, Q = map(int, input().split(' '))
res = [0] * N
for _ in range(Q):
    l, r, t = map(int, input().split(' '))
    for i in range(l-1, r):
        res[i] = t
print('\n'.join([str(i) for i in res]))
