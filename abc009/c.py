N, K = map(int, input().split())
S = input()
T = list(S)


def update():
    change_num = 0
    for j in range(N):
        if S[j] != T[j]:
            change_num += 1
    return change_num


i = 0
change_num = 0
for i in range(N):
    min_char = min(T[i:])
    min_idx = i + ''.join(T[i:]).rfind(min_char)
    if i != min_idx and update() <= K:
        T[min_idx], T[i] = T[i], T[min_idx]
        if update() > K:
            T[i], T[min_idx] = T[min_idx], T[i]
print(''.join(T))
