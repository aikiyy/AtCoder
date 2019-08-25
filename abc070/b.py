a, b, c, d = map(int, input().split())
ans = [0] * 100
for i in range(a, b):
    ans[i] += 1
for i in range(c, d):
    ans[i] += 1
print(len(list(filter(lambda x: x == 2, ans))))