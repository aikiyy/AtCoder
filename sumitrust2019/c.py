X = int(input())
x, y = X//100, X%100

z = 0
for i in range(5, 0, -1):
    z += y // i
    y %= i

if z <= x:
    print(1)
else:
    print(0)
