# -*- coding: utf-8 -*-


if __name__ == '__main__':
    S = input()
    score = _score = [0] * len(S)
    r_num = 0
    l_num = 0
    _s = None
    change_idx = None
    for i, s in enumerate(S):
        if s == 'L' and _s == 'R':
            change_idx = i
        if s == 'R' and _s == 'L':
            #計算
            if r_num == l_num or (r_num + l_num) % 2 == 0:
                score[change_idx - 1] = (r_num + l_num) / 2
                score[change_idx] = (r_num + l_num) / 2
            elif r_num % 2 == 0:
                score[change_idx - 1] = (r_num + l_num) // 2
                score[change_idx] = (r_num + l_num) // 2 + 1
            else:
                score[change_idx - 1] = (r_num + l_num) // 2 + 1
                score[change_idx] = (r_num + l_num) // 2
            #初期化
            r_num = 0
            l_num = 0
            change_idx = None
        if s == 'R':
            r_num += 1
        else:
            l_num += 1
        _s = s

    #計算
    if r_num == l_num or (r_num + l_num) % 2 == 0:
        score[change_idx - 1] = (r_num + l_num) / 2
        score[change_idx] = (r_num + l_num) / 2
    elif r_num % 2 == 0:
        score[change_idx - 1] = (r_num + l_num) // 2
        score[change_idx] = (r_num + l_num) // 2 + 1
    else:
        score[change_idx - 1] = (r_num + l_num) // 2 + 1
        score[change_idx] = (r_num + l_num) // 2

    print(' '.join(map(str, map(int, score))))
