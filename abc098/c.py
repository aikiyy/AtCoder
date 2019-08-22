N = int(input())
S = input()
num = S[1:].count('E')
ans = [num]
for i in range(1, N):
    if S[i] == 'E':
        num -= 1
    if S[i-1] == 'W':
        num += 1
    ans.append(num)
print(min(ans))
