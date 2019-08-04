# -*- coding: utf-8 -*-


if __name__ == '__main__':
    n = int(input())
    num = 0
    for i in range(n):
        if len(str(i+1)) % 2 == 1:
            num += 1
    print(num)
