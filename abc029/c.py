from itertools import product

N = int(input())
char = 'abc'
for i in product(char, repeat=N):
    print(''.join(i))
