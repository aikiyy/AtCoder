# -*- coding: utf-8 -*-


if __name__ == '__main__':
    a, b, c = map(int, input().split(' '))
    print(max(0, c - (a - b)))
