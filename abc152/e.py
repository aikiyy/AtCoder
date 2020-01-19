from fractions import gcd


N = int(input())
A = list(map(int, input().split()))
lcm = lambda x, y: x*y//gcd(x, y)
l = 1
for a in A:
    l = lcm(l, a)
ans = 0
MOD = 10**9+7
for a in A:
    ans += l // a
print(ans % MOD)
