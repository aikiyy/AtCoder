S = input()
R = {'O': '0', 'D': '0', 'I': '1', 'Z': '2', 'S': '5', 'B': '8'}
for k, v in R.items():
    S = S.replace(k, v)
print(S)
