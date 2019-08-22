N = int(input())
a = list(map(int, input().split()))
m = sum(a[:1])
n = sum(a[1:])
ans = [abs(m-n)]
for i in range(1, N-1):
    m += a[i]
    n -= a[i]
    ans.append(abs(m-n))
print(min(ans))