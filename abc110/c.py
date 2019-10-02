from collections import Counter

S = Counter(list(input()))
T = Counter(list(input()))

flag = False
for s, t in zip(S.most_common(), T.most_common()):
    if s[1] != t[1]:
        flag = True
print('No' if flag else 'Yes')
