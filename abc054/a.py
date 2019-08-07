a, b = map(int, input().split(' '))
a, b = (map(lambda x: x + 13 if x == 1 else x, [a, b]))
if a == b:
    print('Draw')
elif a > b:
    print('Alice')
else:
    print('Bob')