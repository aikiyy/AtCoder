n, x = map(int, input().split())
a = list(map(int, input().split()))

ba = sum(a)
if a[0] > x:
    a[0] = x
for i in range(n-1):
    if a[i] + a[i+1] <= x:
        continue
    a[i+1] = x - a[i]
print(ba - sum(a))
