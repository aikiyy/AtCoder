# -*- coding: utf-8 -*-


N = int(input())
num = 0
for _ in range(N):
    l, r = map(int, input().split(' '))
    num += r - l + 1
print(num)
