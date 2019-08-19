n, x = map(int, input().split())
x = list(map(lambda y: abs(x - int(y)), input().split()))


from functools import reduce
# from math import gcd
from fractions import gcd
def greatest_common_divisor(iter):
    '''
    最大公約数を返す
    '''
    return reduce(gcd, iter)


print(greatest_common_divisor(x))
