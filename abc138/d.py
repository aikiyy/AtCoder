n, q = map(int, input().split())
# tree = [list(map(int, input().split())) for i in range(n-1)]
edges = [set() for i in range(n)]
for _ in range(n-1):
    a, b= map(int,input().split())
    edges[a-1].add(b-1)
cnt = [0] * n

for _ in range(q):
    p, x = map(int, input().split())
    cnt[p-1] += x

l = [0]
l2 = [cnt[0]]
while len(l) != 0:
    a = l.pop()
    b = l2.pop()
    if a != 0:
        cnt[a] += b
    for i in edges[a]:
        l.append(i)
        l2.append(cnt[a])
print(*cnt)
