n = int(input())
a = [0] * 3
a[0], a[1], a[2] = 0, 0, 1
if n <= 3:
    print(a[n-1])
    exit()
for _ in range(3, n):
    _a = sum(a) % 10007
    a[2], a[1], a[0] = _a, a[2], a[1]
print(a[2] % 10007)