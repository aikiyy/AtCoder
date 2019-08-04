# -*- coding: utf-8 -*-


def move(s, score):
    new_score = [0] * len(s)
    for i, v in enumerate(score):
        if v == 0:
            continue
        if s[i] == 'R':
            new_score[i + 1] += v
        else:
            new_score[i - 1] += v
    return new_score


if __name__ == '__main__':
    s = input()
    score = _score = [1] * len(s)
    i = 0
    while True:
        tmp_score = score
        score = move(s, score)
        if score == _score:
            if i % 2 == 0:
                score = move(s, score)
            break
        _score = tmp_score
        i += 1
    print(' '.join(map(str, score)))
