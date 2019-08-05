# -*- coding: utf-8 -*-


N, M = map(int, input().split(' '))
intersection = None
for _ in range(N):
    k, *a = map(int, input().split(' '))
    if intersection is None:
        intersection = set(a)
    else:
        intersection = intersection & set(a)

print(len(intersection))
