D, N = map(int, input().split())
if D == 0:
    base = 1
elif D == 1:
    base = 100
elif D == 2:
    base = 10000
print(base * N)
