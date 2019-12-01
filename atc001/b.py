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


N, Q = map(int, input().split())
uf = UnionFind(N)
for _ in range(Q):
    p, a, b = map(int, input().split())
    if p == 0:
        uf.union(a, b)
    else:
        print('Yes' if uf.same(a, b) else 'No')
