from collections import Counter


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

wrong_num = 0
for i in range(N):
    if A[i] > B[i]:
        wrong_num += 1
if wrong_num > N-2:
    print('No')
    exit()

c_a = Counter(A)
c_b = Counter(B)

for k, v in c_b.items():
    t = sum([v2 for k2, v2 in c_a.items() if k2 <= k])
    if t < v:
        print('No')
        exit()
print('Yes')
