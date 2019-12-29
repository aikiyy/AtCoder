N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()


RSP = ['r', 's', 'p']
ANS = ['p', 'r', 's']
ANS_SCORE = [P, R, S]
hands = []
ans = 0
for i in range(N):
    # K回前をきにする
    if i >= K:
        idx = RSP.index(T[i])
        if hands[-K] == ANS[idx]:
            hands.append('x')
        else:
            hands.append(ANS[idx])
            ans += ANS_SCORE[idx]
    else:
        idx = RSP.index(T[i])
        hands.append(ANS[idx])
        ans += ANS_SCORE[idx]
print(ans)
