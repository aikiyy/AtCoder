# -*- coding: utf-8 -*-

N, T = map(int, input().split(' '))
costs = []
for _ in range(N):
    c, t = map(int, input().split(' '))
    if t <= T:
        costs.append(c)

if len(costs) == 0:
    print('TLE')
else:
    print(min(costs))