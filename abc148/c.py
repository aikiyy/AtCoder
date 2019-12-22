from functools import reduce
from fractions import gcd


def least_common_multiple(iter):
    '''
    最小公倍数を返す
    '''
    lcm = lambda x, y: x*y//gcd(x, y)
    return reduce(lcm, iter)


AB = map(int, input().split())
print(least_common_multiple(AB))
