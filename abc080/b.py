n = int(input())
if n % sum(map(int, str(n))) == 0:
    print('Yes')
else:
    print('No')