import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())

red = set()
for x in range(x1-r, x1+r+1):
    for y in range(y1-r, y1+r+1):
        if distance(x, y, x1, y1) <= r:
            red.add(tuple([x, y]))

blue = set()
for x in range(x2, x3+1):
    for y in range(y2, y3+1):
        blue.add(tuple([x, y]))

print('YES' if len(red-blue) != 0 else 'NO')
print('YES' if len(blue-red) != 0 else 'NO')
