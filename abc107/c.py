n, k = map(int, input().split())
x = list(map(int, input().split()))
ans = []
for i in range(n-k+1):
    l = x[i]
    r = x[i+k-1]
    ans.append(min(abs(l) + abs(r-l), abs(r) + abs(l-r)))
print(min(ans))
