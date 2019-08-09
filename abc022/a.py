n, s, t = map(int, input().split(' '))
w = int(input())
a = [w]
for _ in range(n-1):
    a.append(a[-1] + int(input()))
print(len(list(filter(lambda x: x >= s and x <= t, a))))