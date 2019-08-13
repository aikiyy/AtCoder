s = map(int, input())
l = []
ans = 0
for i in s:
    if len(l) != 0 and l[-1] != i:
        l.pop()
        ans += 2
    else:
        l.append(i)
print(ans)