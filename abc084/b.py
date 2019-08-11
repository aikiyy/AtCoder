a, b = map(int, input().split(' '))
s = list(map(lambda x: len(x), input().split('-')))
print('Yes' if len(s) == 2 and s[0] == a and s[1] == b else 'No')