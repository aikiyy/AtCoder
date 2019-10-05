S = input()
c = S[0]
ans = 0
for s in S[1:]:
    if s != c:
        ans += 1
    c = s
print(ans)
