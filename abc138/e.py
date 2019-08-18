S = input()
T = input()

if not set(S) >= set(T):
    print('-1')
    exit()

idxs = list()
for t in T:
    idx = set()
    for i, s in enumerate(S):
        if t == s:
            idx.add(i)
    idxs.append(idx)

str_repeat_num = 0
now_idx = 0
for i, t in enumerate(T):
    l = list(filter(lambda x: x > now_idx, idxs[i]))
    if len(l) != 0:
        now_idx = l[0]
    else:
        str_repeat_num += 1
        now_idx = idxs[i].pop()
print(len(S) * str_repeat_num + now_idx + 1)
