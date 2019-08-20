S = input()

ans = 0
if len(S) == 1:
    ans = int(S)
else:
    for i in range(2**(len(S)-1)):
        tmp = S[0]
        for j, b in enumerate(format(i, 'b').zfill(len(S)-1)):
            if b == '1':
                tmp += '+'
            tmp += S[j+1]
        ans += eval(tmp)
print(ans)
