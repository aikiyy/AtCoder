from itertools import groupby

S = input()
print(''.join([k + str(len(list(g))) for k, g in groupby(S)]))
