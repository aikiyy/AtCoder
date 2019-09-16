S = input()
if 'L' in [S[i] for i in range(0, len(S), 2)] or 'R' in [S[i] for i in range(1, len(S), 2)]:
    print('No')
else:
    print('Yes')
