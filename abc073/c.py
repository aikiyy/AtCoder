# a = [int(input()) for _ in range(int(input()))]
# print(sum([1 for i in set(a) if a.count(i) % 2 == 1]))

A = {}
for _ in range(int(input())):
    a = input()
    A[a] = A.get(a, 0) + 1

print(len(list(filter(lambda x: x % 2 != 0, A.values()))))