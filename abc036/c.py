a = [int(input()) for _ in range(int(input()))]
d = {}
for i, v in enumerate(sorted(set(a))):
    d[v] = i

for i in a:
    print(d[i])
