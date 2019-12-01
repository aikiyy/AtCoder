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


N, K, L = map(int, input().split())
ufk = UnionFind(N)
for _ in range(K):
    p, q = map(int, input().split())
    ufk.union(p, q)
ufl = UnionFind(N)
for _ in range(L):
    r, s = map(int, input().split())
    ufl.union(r, s)

d = {}
for i in range(1, N+1):
    k_par = ufk.find(i)
    l_par = ufl.find(i)
    d[(k_par, l_par)] = d.get((k_par, l_par), 0) + 1

ans = []
for i in range(1, N+1):
    ans.append(d[(ufk.find(i), ufl.find(i))])
print(*ans)
