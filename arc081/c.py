from collections import Counter

N = int(input())
A = Counter(list(map(int, input().split())))
A = {k: v for k, v in A.items() if v >= 2}
A = sorted(A.items(), key=lambda x: x[0], reverse=True)
A.extend([(0, 0), (0, 0)])
if A[0][1] >= 4:
    print(A[0][0]**2)
else:
    print(A[0][0]*A[1][0])
