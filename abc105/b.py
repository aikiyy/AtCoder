n = int(input())
ans = False
for i in range(n//4 + 1):
    for j in range(n//7 + 1):
        if 4*i+7*j == n:
            ans = True
print('Yes' if ans else 'No')
