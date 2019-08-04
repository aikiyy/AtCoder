# -*- coding: utf-8 -*-


if __name__ == '__main__':
    n = int(input())
    h = list(map(int, input().split(' ')))
    _num = 0
    _flag = False
    for num in h:
        if _num > num:
            _flag = True
            break
        elif _num != num:
            _num = num - 1


    if _flag:
        print('No')
    else:
        print('Yes')
