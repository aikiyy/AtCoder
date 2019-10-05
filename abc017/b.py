X = input()
R = {'ch': '', 'o': '', 'k': '', 'u': ''}
for k, v in R.items():
    X = X.replace(k, v)
print('YES' if len(X) == 0 else 'NO')
