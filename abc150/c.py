from itertools import permutations


N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

for i, p in enumerate(permutations(range(1, N+1))):
    if list(p) == P:
        p_num = i
    if list(p) == Q:
        q_num = i
print(abs(p_num-q_num))
