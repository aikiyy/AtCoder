N = int(input())

if N & 1:
    print(0)
else:
    k = 10
    ans = 0
    while k <= N:
        ans += N // k
        k *= 5
    print(ans)
