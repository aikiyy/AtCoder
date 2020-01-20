from functools import reduce
from fractions import gcd


def least_common_multiple(iter):
    '''
    最小公倍数を返す
    '''
    lcm = lambda x, y: x*y//gcd(x, y)
    return reduce(lcm, iter)


N, M = map(int, input().split())
A = list(map(int, input().split()))
l = least_common_multiple(map(lambda x: x//2, A))

div_num = 0
num = A[0]
flag = False
while num % 2 == 0:
    num = num // 2
    div_num += 1
for a in A:
    cnt = 0
    while a % 2 == 0:
        a = a // 2
        cnt += 1
    if div_num != cnt:
        flag = True

baisuu = M // l
if flag:
    print(0)
elif baisuu & 1:
    print((baisuu + 1)//2)
else:
    print(baisuu//2)
