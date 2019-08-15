import collections


n = int(input())
A = input().split()
d = collections.defaultdict(int)
for a in A:
    d[a] += 1
if n == 1:
    print(1)
    exit()
if n % 2 != 0:
    if '0' not in d or d['0'] != 1:
        print(0)
        exit()
    for i in range(2, n, 2):
        if str(i) not in d or d[str(i)] != 2:
            print(0)
            exit()
else:
    if '0' in d:
        print(0)
        exit()
    for i in range(1, n, 2):
        if str(i) not in d or d[str(i)] != 2:
            print(0)
            exit()
print(2**(n//2) % (10**9+7))

