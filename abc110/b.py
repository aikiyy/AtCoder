N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

z = list(range(max(x)+1, min(y)+1))
if len(list(filter(lambda x: X < x <= Y, z))) == 0:
    print('War')
else:
    print('No War')
