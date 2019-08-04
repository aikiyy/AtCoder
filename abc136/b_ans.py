# -*- coding: utf-8 -*-


if __name__ == '__main__':
    N = int(input())
    print(len(list(filter(lambda x: len(str(x)) % 2 == 1, range(1, N + 1)))))
