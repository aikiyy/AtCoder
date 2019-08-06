a, b = input().split(' ')
num = int(a + b)
if num == int(int(num**.5)**2):
    print('Yes')
else:
    print('No')