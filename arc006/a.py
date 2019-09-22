E = list(map(int, input().split()))
B = int(input())
L = list(map(int, input().split()))

itti = 0
for l in L:
    if l in E:
        itti += 1

if itti == 6:
    print(1)
elif itti == 5 and B in L:
    print(2)
elif itti >= 3:
    print(8 - itti)
else:
    print(0)
