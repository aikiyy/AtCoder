n, k = [int(input()) for _ in range(2)]
ans = 1
for _ in range(n):
    if ans > k:
        ans += k
    else:
        ans *= 2
print(ans)