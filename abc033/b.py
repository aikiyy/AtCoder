# -*- coding: utf-8 -*-


N = int(input())

max_str = None
max_p = 0
sum_p = 0
for _ in range(N):
    s, p = input().split(' ')
    p = int(p)
    if p > max_p:
        max_p = p
        max_str = s
    sum_p += p

if max_p > sum_p // 2:
    print(max_str)
else:
    print('atcoder')
