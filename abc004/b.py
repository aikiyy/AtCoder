C = []
for _ in range(4):
    C.append(list(map(str, input())))

for c in C[::-1]:
    print(' '.join(map(str, c[::-1])))
