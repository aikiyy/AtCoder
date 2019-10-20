def solve(s):
    n = len(s)
    k = 0
    ans = 0
    while n >= 5:
        if s[k:k+5] in ('tokyo', 'kyoto'):
            ans += 1
            k += 5
            n -= 5
        else:
            k += 1
            n -= 1
    return ans


T = int(input())
for _ in range(T):
    print(solve(input()))
