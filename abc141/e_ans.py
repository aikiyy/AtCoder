N = int(input())
S = input()

ans = 0
len_s = 1
for i in range(N):
    tmp_s = S[i:i+len_s]
    while tmp_s in S[i+len_s:]:
        len_s += 1
        tmp_s = S[i:i+len_s]
        ans += 1
print(ans)
