*a, = list(map(int, input().split(' ')))
if 1.0 * a[1] / a[0] > 1.0 * a[3] / a[2]:
    print('TAKAHASHI')
elif 1.0 * a[1] / a[0] < 1.0 * a[3] / a[2]:
    print('AOKI')
else:
    print('DRAW')