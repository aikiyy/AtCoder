S = input()
T = input()

if not set(S) >= set(T):
    print(-1)
    exit()

str_repeat_num = 0
now_idx = 0
for t in T:
    idx = set()
    for i, s in enumerate(S[now_idx:]):
        if t == s:
            now_idx = i + 1 + now_idx
            break
    else:
        str_repeat_num += 1
        for i, s in enumerate(S[:now_idx]):
            if t == s:
                now_idx = i
print(len(S) * str_repeat_num + now_idx)
