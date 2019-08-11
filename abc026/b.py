import math


n = int(input())
r = sorted([int(input()) for _ in range(n)], reverse=True)
print(sum(map(lambda x: x[1] ** 2 if x[0] % 2 == 0 else -1 * (x[1] ** 2), enumerate(r))) * math.pi)
