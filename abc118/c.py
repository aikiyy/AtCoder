from functools import reduce
from fractions import gcd


n = int(input())
a = list(map(int, input().split()))
print(reduce(gcd, a))