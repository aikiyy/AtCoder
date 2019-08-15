n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)
a.append(0)

c = 0
for i in range(n+1):
    c += abs(a[i+1] - a[i])

for i in range(1, n+1):
    print(c - abs(a[i-1] - a[i]) - abs(a[i] - a[i+1]) + abs(a[i-1] - a[i+1]))
