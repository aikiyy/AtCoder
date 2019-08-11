s = input()
n = int(input())

names = []
for i in range(5):
    for j in range(5):
        names.append(s[i]+s[j])

print(sorted(names)[n-1])