n = int(input())
a0, a1 = 2, 1
for _ in range(1, n):
    a0, a1 = a1, a0+a1
print(a1)