N = int(input())
S = input()

ans = 'b'
for i in range(1, len(S)//2 + 1):
    if i % 3 == 1:
        ans = 'a' + ans + 'c'
    elif i % 3 == 2:
        ans = 'c' + ans + 'a'
    else:
        ans = 'b' + ans + 'b'
print(len(S)//2 if S == ans else -1)
