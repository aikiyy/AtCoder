n, m = map(int, input().split())
A = [int(input()) for _ in range(m)][::-1]

ans = []
s = set()
for a in A:
    if a not in s:
        ans.append(a)
    s.add(a)
for i in range(1, n+1):
    if i not in s:
        ans.append(i)
print('\n'.join(map(str, ans)))