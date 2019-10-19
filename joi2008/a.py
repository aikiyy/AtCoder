n = 1000 - int(input())
coin = [500, 100, 50, 10, 5, 1]

ans = 0
for c in coin:
    a, n = divmod(n, c)
    ans += a
    if n == 0:
        break
print(ans)
