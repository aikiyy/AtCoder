X, Y = map(int, input().split())
ans = 1
while X < Y:
    X = X * 2
    if X <= Y:
        ans += 1
print(ans)
