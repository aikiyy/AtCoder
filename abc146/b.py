upper = [chr(i) for i in range(65, 65+26)]

N = int(input())
S = input()

ans = []
for s in S:
    idx = upper.index(s)
    ans.append(upper[(idx+N)%26])
print(''.join(ans))
