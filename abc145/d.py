def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result = result * int(numerator[k]) % 1000000007
    return result


X, Y = map(int, input().split())

if (X+Y)%3 != 0 or X < Y / 2 or Y < X / 2:
    print(0)
    exit()

num = (X + Y) // 3
ans = cmb(num, X-num)
print(ans)
