n = int(input())
S = []
for _ in range(n):
    S.append(list(map(str, input())))

for s in zip(*S):
    print(''.join(s[::-1]))
