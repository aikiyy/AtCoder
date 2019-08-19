import heapq


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


from functools import reduce
from math import gcd
def greatest_common_divisor(iter):
    '''
    最大公約数を返す
    '''
    return reduce(gcd, iter)