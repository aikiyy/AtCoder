N, A, B = map(int, input().split())
ans = 0
for _ in range(N):
    s, d = input().split()
    move = min(max(A, int(d)), B)
    if s == 'East':
        ans += move
    else:
        ans -= move
if ans == 0:
    print(0)
elif ans < 0:
    print('West {}'.format(abs(ans)))
else:
    print('East {}'.format(abs(ans)))
