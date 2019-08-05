# -*- coding: utf-8 -*-

n = int(input())
P = sorted(list([int(input()) for _ in range(n)]))
cost = P[-1] / 2 + sum(P[:-1])
print(int(cost))