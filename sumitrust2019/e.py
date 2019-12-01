N = int(input())
A = list(map(int, input().split()))

X = [-1, -1, -1]
ans = 1
for a in A:
    t = X.count(a-1)
    ans = ans * t % 1000000007
    if a-1 not in X:
        print(0)
        exit()
    idx = X.index(a-1)
    X[idx] += 1
print(ans)
