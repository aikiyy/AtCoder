S = input()
T = int(input())

dis = abs(S.count('R') - S.count('L')) + abs(S.count('U') - S.count('D'))
if T == 1:
    print(dis + S.count('?'))
else:
    print(max(len(S) % 2, dis - S.count('?')))
