from functools import reduce
from fractions import gcd


def greatest_common_divisor(iter):
    '''
    最大公約数を返す
    '''
    return reduce(gcd, iter)


N, K = map(int, input().split())
A = list(map(int, input().split()))

if K % greatest_common_divisor(A) != 0 or K > max(A):
    print('IMPOSSIBLE')
else:
    print('POSSIBLE')