from math import factorial


W, H = map(int, input().split())
m = 10**9 + 7
print((factorial(W+H-2) * pow(factorial(W-1) * factorial(H-1) % m, m-2, m)) % m)
