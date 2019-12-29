import heapq
from functools import reduce
from fractions import gcd


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


def is_prime(n):
    '''
    素数判定する
    '''
    if n == 1:
        return False
    for k in range(2, int(n**0.5) + 1):
        if n % k == 0:
            return False
    return True


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


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)


'''
ツリー探索
'''
N = 1000
root = 0
G = [[] for _ in range(N)]
def dfs(v, p):
    for nv in G[v]:
        if nv == p:
            continue
        dfs(nv, v)
dfs(root, -1)


'''
二部グラフ判定
'''
colors = []
edges = []
# 頂点vをcolor(1 or -1)で塗り、矛盾がないか調べる
# dfs(0, 1)がTrueなら二部グラフ
def dfs(v, color):
    colors[v] = color
    for to in edges[v]:
        # 同じ色が隣接するならFalse
        if colors[to] == color:
            return False
        # 未着手の頂点は反転した色を指定
        if colors[to] == 0 and not dfs(to, -color):
            return False
    return True


'''
ダイクストラ法
'''
def dijkstra(n, s, adj_list):
    # 始点sから各頂点への最短距離
    # n: 頂点数, adj_list:各頂点が(先のノード, cost)を持ったリスト
    from heapq import heappush, heappop

    dists = [float('inf')] * n
    dists[s] = 0
    heap, rem = [(0, s)], n - 1

    while heap and rem:
        cost, src = heappop(heap)
        if dists[src] < cost:
            continue
        rem -= 1

        for dest, _cost in adj_list[src]:
            newcost = cost + _cost
            if dists[dest] > newcost:
                dists[dest] = newcost
                heappush(heap, (newcost, dest))

    return dists


'''
最小全域木(prim法)
'''
def prim(n, s, edges):
    # n:頂点数, s:スタートノード
    # edges: edgeリスト(cost, 行き先ノード)
    used = [False] * n
    edgelist = []
    for e in edges[s]:
        heapq.heappush(edgelist, e)
    used[s] = True
    res = 0
    while len(edgelist) != 0:
        minedge = heapq.heappop(edgelist)
        if used[minedge[1]]:
            continue
        used[minedge[1]] = True
        for e in edges[minedge[1]]:
            if not used[e[1]]:
                heapq.heappush(edgelist, e)
        res += minedge[0]
    return res


'''
牛ゲー
最短経路問題
'''
def bellman_ford(edges, n, src):
    # n:ノード数, src:スタートノード
    # edges:edge(src, tgt, cost)のリスト
    inf = float('inf')
    dist = [inf for _ in range(n)]
    dist[src] = 0
    # 移動経路
    pre = {}

    # 最短経路算出
    for i in range(n-1):
        for edge in edges:
            # srcにコストがあり、tgtのコストよりも低いコストで更新できそうなら
            if dist[edge[0]] != inf and dist[edge[1]] > dist[edge[0]] + edge[2]:
                dist[edge[1]] = dist[edge[0]] + edge[2]
                pre[edge[1]] = edge[0]

    # 負の閉路検出
    def checkpath(pre, n, src):
        if src in pre and pre[n-1] == src and pre[src] == n-1:
            return True
        count = 0
        p = pre[n-1]
        while p != src:
            p = pre[p]
            if p == src and src in pre:
                return True
            count += 1
            if count >= n-1:
                return True
        return False

    is_cycle = checkpath(pre, n, src)
    return (dist, is_cycle)