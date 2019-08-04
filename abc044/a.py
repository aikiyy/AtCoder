# -*- coding: utf-8 -*-


if __name__ == '__main__':
    n, k, x, y = [int(input()) for _ in range(4)]
    print(min(n, k) * x + max(n - k, 0) * y)