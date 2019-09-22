S = input()
ans = 0
count = 0 if S[0] == 'B' else 1
for i in range(1, len(S)):
    if S[i] == 'W':
        ans += i - count
        count += 1
print(ans)
