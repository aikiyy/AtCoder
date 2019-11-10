from collections import Counter


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
max_a = max(A)
max_b = max(B)

if max_a > max_b:
    print('No')
    exit()

wrong_num = 0
for i in range(N):
    if A[i] > B[i]:
        wrong_num += 1
if wrong_num > N-2:
    print('No')
    exit()

c_a = sorted(Counter(A).items())
c_b = sorted(Counter(B).items())

idx = 0
total_a = 0
total_b = 0
len_c_a = len(c_a)
for k, v in c_b:
    while idx < len_c_a and c_a[idx][0] <= k:
        total_a += c_a[idx][1]
        idx += 1
    total_b += v
    if total_a < total_b:
        print('No')
        exit()
print('Yes')
