a, b = map(int, input().split(' '))
print('16:9' if a % 16 == b % 9 else '4:3')
