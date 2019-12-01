import math


N = int(input())
for i in range(50000):
    x = math.floor(i * 1.08)
    if x == N:
        print(i)
        exit()
print(':(')
