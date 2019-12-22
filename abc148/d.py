N = int(input())
A = map(int, input().split())

idx = 1
ans = 0
for a in A:
    if a == idx:
        idx += 1
    else:
        ans += 1

if ans == N:
    print(-1)
else:
    print(ans)
