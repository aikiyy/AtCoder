a = []
a.append(int(input()))

while a[-1] not in a[:-1]:
    if a[-1] % 2 == 0:
        a.append(a[-1]//2)
    else:
        a.append(3*a[-1] + 1)
print(len(a))
