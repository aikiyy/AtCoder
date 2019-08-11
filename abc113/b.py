n = int(input())
t, a = map(int, input().split(' '))
h = list(map(lambda x: abs(a - (t - 0.006 * int(x))), input().split(' ')))
print(h.index(min(h)) + 1)
