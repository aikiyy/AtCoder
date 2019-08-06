import math


n = int(input())
*a, = map(int, input().split(' '))
print(math.ceil(sum(a) / len(list(filter(lambda x: x > 0, a)))))
