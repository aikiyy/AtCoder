n = int(input())
a = list(range(1, 7))
for i in range(n%30):
    a[i%5], a[i%5+1] = a[i%5+1], a[i%5]
print(*a, sep='')