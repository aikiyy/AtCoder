n = int(input())
a = [int(input()) - 1 for _ in range(n)]

i = 0
ans = 1
while a[i] != -1:
    if a[i] == 1:
        print(ans)
        exit()
    _i = a[i]
    a[i] = -1
    i = _i
    ans += 1
print(-1)