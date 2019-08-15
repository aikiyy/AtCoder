n = int(input())
a = list(filter(lambda x: x % 2 == 0, map(int, input().split())))
ans = 0
while len(a) != 0:
    ans += len(a)
    a = list(filter(lambda x: x % 2 == 0, map(lambda x: x / 2, a)))
print(ans)