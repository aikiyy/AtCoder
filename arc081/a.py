from collections import Counter

N = int(input())
A = Counter(list(map(int, input().split())))

ans = [0, 0]
for k in sorted(A.keys(), reverse=True):
    if A[k] >= 2:
        ans.append(k)
    if A[k] >= 4:
        ans.append(k)
ans = sorted(ans)
print(ans[-1]*ans[-2])
