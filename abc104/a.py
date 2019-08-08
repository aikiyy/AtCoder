r = int(input())
if r < 1200:
    print('ABC')
elif r < 2800:
    print('ARC')
else:
    print('AGC')

# print(['ABC', 'ARC', 'AGC'][int(input())//50+8>>5])