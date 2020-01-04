import math


A, B, C = map(int, input().split())

l = 0
r = 100
f = lambda t: A * t + B * math.sin(C * t * math.pi)

while True:
    t = (l + r) / 2
    if abs(f(t) - 100) <= pow(10, -6):
        break
    if f(t) >= 100:
        r = t
    else:
        l = t
print(t)
