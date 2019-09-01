import math


N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

ans = 0

# plus plus
x = 0
y = 0
for xy in XY:
    if xy[0] >= 0 and xy[1] >= 0:
        x += xy[0]
        y += xy[1]
    elif xy[0] <= 0 and xy[1] <= 0:
        continue
    else:
        if x + y <= x + y + xy[0] + xy[1]:
            x += xy[0]
            y += xy[1]
ans = max(ans, math.sqrt(x**2 + y**2))

# plus minus
x = 0
y = 0
for xy in XY:
    if xy[0] >= 0 and xy[1] <= 0:
        x += xy[0]
        y += xy[1]
    elif xy[0] <= 0 and xy[1] >= 0:
        continue
    else:
        if x - y <= x - y + xy[0] - xy[1]:
            x += xy[0]
            y += xy[1]
ans = max(ans, math.sqrt(x**2 + y**2))

# minus plus
x = 0
y = 0
for xy in XY:
    if xy[0] <= 0 and xy[1] >= 0:
        x += xy[0]
        y += xy[1]
    elif xy[0] >= 0 and xy[1] <= 0:
        continue
    else:
        if -x + y <= -x + y - xy[0] + xy[1]:
            x += xy[0]
            y += xy[1]
ans = max(ans, math.sqrt(x**2 + y**2))

# minus minus
x = 0
y = 0
for xy in XY:
    if xy[0] <= 0 and xy[1] <= 0:
        x += xy[0]
        y += xy[1]
    elif xy[0] >= 0 and xy[1] >= 0:
        continue
    else:
        if -x - y <= -x - y - xy[0] - xy[1]:
            x += xy[0]
            y += xy[1]
ans = max(ans, math.sqrt(x**2 + y**2))

print(ans)
