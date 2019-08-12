n, m = map(int, input().split())
sa = set()
sb = set()
for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        sb.add(b)
    if b == n:
        sa.add(a)

print('POSSIBLE' if len(sa&sb) != 0 else 'IMPOSSIBLE')
