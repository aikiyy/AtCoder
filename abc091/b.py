# -*- coding: utf-8 -*-
from collections import Counter


if __name__ == '__main__':
    n = int(input())
    s = [input() for _ in range(n)]
    m = int(input())
    t = [input() for _ in range(m)]
    s_set = set(s)
    print(max(0, max([s.count(i) - t.count(i) for i in s_set])))
