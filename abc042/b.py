# -*- coding: utf-8 -*-


if __name__ == '__main__':
    n, l = map(int, input().split())
    s = sorted([input() for _ in range(n)])
    print(''.join(s))
