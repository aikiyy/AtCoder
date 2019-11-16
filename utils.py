import heapq
from functools import reduce
from math import gcd


class Reverse:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

    def __repr__(self):
        return repr(self.val)


class Heapq:
    def __init__(self, arr, desc=False):
        if desc:
            for i in range(len(arr)):
                arr[i] = Reverse(arr[i])
        self.desc = desc
        self.hq = arr
        heapq.heapify(self.hq)

    def pop(self):
        if len(self.hq) == 0:
            return None
        if self.desc:
            return heapq.heappop(self.hq).val
        else:
            return heapq.heappop(self.hq)

    def push(self, a):
        if self.desc:
            heapq.heappush(self.hq, Reverse(a))
        else:
            heapq.heappush(self.hq, a)

    def top(self):
        if self.desc:
            return self.hq[0].val
        else:
            return self.hq[0]

    def __len__(self):
        return len(self.hq)


def euclidean(x, y):
    '''
    最大公約数を返す
    '''
    x, y = max(x, y), min(x, y)
    while y != 0:
        x, y = y, x%y
    return x


def greatest_common_divisor(iter):
    '''
    最大公約数を返す
    '''
    return reduce(gcd, iter)


def least_common_multiple(iter):
    '''
    最小公倍数を返す
    '''
    lcm = lambda x, y: x*y//gcd(x, y)
    return reduce(lcm, iter)


def make_divisors(n):
    '''
    nの約数リストを返す
    '''
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    # divisors.sort()
    return divisors


def trial_division(n):
    '''
    素因数分解する
    '''
    factor = []
    for num in range(2, int(n**0.5)+1):
        while n % num == 0:
            n //= num
            factor.append(num)
    if not factor or n != 1:
        factor.append(n)
    return factor


def cmb(n, r):
    '''
    高速にnCrを計算する
    '''
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2, r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
    return result
