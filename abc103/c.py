from collections import Counter

N = int(input())
V = list(map(int, input().split()))
S1 = Counter([V[i] for i in range(0, N, 2)])
S2 = Counter([V[i] for i in range(1, N, 2)])

S1 = sorted(S1.items(), key=lambda x: x[1], reverse=True)
S2 = sorted(S2.items(), key=lambda x: x[1], reverse=True)
S1.append([0, 0])
S2.append([0, 0])

if S1[0][0] == S2[0][0]:
    ans = min(N-(S1[0][1]+S2[1][1]), N-(S1[1][1]+S2[0][1]))
else:
    ans = N - (S1[0][1] + S2[0][1])
print(ans)
