from collections import Counter

N = int(input())
S = Counter(list(map(int, input().split())))
ans = 0
for k, v in S.items():
    if k < v:
        ans += v-k
    elif k > v:
        ans += v
print(ans)
