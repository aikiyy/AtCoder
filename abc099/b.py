a, b = map(int, input().split())

x, y = 1, 3
while True:
    ax = x - a
    by = y - b
    if ax == by and ax >= 0 and by >= 0:
        break
    x, y = y, y + (y - x) + 1
print(ax)
