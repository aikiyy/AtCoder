import string
S = input()
for s in string.ascii_lowercase:
    if s not in S:
        print(s)
        break
else:
    print('None')