n = int(input())
A = list(map(int, input().split()))
# TLE
# l = []
# for i, a in enumerate(A):
#     if i%2 == 0:
#         l.append(a)
#     else:
#         l.insert(0, a)
# print(' '.join(map(str, l)))

print(' '.join(map(str, A[::-2])), ' '.join(map(str, A[n%2::2])))
