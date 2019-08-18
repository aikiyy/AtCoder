n, m = map(int, input().split())
edges = {tuple(sorted(map(int, input().split()))) for _ in range(m)}

ans = 0
for x in edges:
    l = list(range(n))
    for y in edges:
        if y == x:
            continue
        l = [l[y[0]-1] if l[i] == l[y[1]-1] else l[i] for i in range(n)]
    if set(l) != 1:
        ans += 1
print(ans)