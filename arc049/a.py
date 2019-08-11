s = input()
for i, v in enumerate(map(int, input().split(' '))):
    s = s[:v+i] + '"' + s[v+i:]
print(s)