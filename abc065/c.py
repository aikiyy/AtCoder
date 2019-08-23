from math import factorial


N, M = map(int, input().split())
m = 10**9 + 7
if abs(N-M) >= 2:
    print(0)
elif abs(N-M) == 1:
    print(factorial(N) * factorial(M) % m)
else:
    print(2 * factorial(N) * factorial(M) % m)
