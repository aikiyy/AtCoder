# -*- coding: utf-8 -*-


a, b = [int(input()) for _ in range(2)]
x = abs(a - b)
print(min(x, 10 - x))
