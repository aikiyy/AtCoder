from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))
S = Counter(A)

ans = 0
S = sorted(S.items(), key=lambda x: x[1])
for i in range(len(S)-K):
    ans += S[i][1]
print(ans)
