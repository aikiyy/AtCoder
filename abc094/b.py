# -*- coding: utf-8 -*-


N, M, X = map(int, input().split(' '))
AM = list(map(int, input().split(' ')))
cost = len(list(filter(lambda x: x < X, AM)))
print(min(cost, len(AM) - cost))