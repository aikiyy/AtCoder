# -*- coding: utf-8 -*-


if __name__ == '__main__':
    n = int(input())
    d = list([int(input()) for _ in range(n)])
    print(len(set(d)))
