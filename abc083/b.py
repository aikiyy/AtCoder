n, a, b = map(int, input().split())
ans = 0
for i in range(1, n+1):
    c = sum(map(int, str(i)))
    if a <= c <=b:
        ans += i
print(ans)