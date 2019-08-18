S = input()
T = input()

if not set(S) >= set(T):
    print(-1)
    exit()

str_repeat_num = 0
now_idx = 0
for t in T:
    if t in S[now_idx:]:
        now_idx += S[now_idx:].index(t) + 1
    else:
        str_repeat_num += 1
        now_idx = now_idx = S[:now_idx].index(t) + 1
print(len(S) * str_repeat_num + now_idx)
