n = int(input())
a = list(map(int, input().split(' ')))

ans = 0
while len(list(filter(lambda x: x%2 == 1, a))) == 0:
    a = list(map(lambda x: int(x/2), a))
    ans += 1
print(ans)