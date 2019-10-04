from collections import Counter

N = int(input())
S = Counter([input() for _ in range(N)])
print(S.most_common()[0][0])
