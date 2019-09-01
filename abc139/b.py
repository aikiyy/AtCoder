import math


A, B = map(int, input().split())
ans = 0
while True:
    if ans == 0:
        tap = 1
    elif ans == 1:
        tap = A
    else:
        tap = A + (A-1) * (ans - 1)
    if tap >= B:
        break
    ans += 1
print(ans)
