# -*- coding: utf-8 -*-


if __name__ == '__main__':
    *a, = map(int, input().split(' '))
    print(max(a) - min(a))
