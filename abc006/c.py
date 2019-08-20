n, m = map(int, input().split())
if 2*n <= m <= 4*n:
    y = m%2
    z = ((m-3*y) - 2*(n-y)) // 2
    x = n-y-z
    print(x, y, z)
else:
    print('-1 -1 -1')