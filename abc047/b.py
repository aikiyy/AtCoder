w, h, n = map(int, input().split())
b = 0
c = 0
for _ in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        b = max(b, x)
    elif a == 2:
        w = min(w, x)
    elif a == 3:
        c = max(c, y)
    elif a == 4:
        h = min(h, y)
print(max(0, (w-b)) * max(0, (h-c)))
