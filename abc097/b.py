x = int(input())
max_num = 0
for b in range(1, 33):
    for p in range(2, 33):
        if b**p > x:
            continue
        max_num = max(max_num, b**p)
print(max_num)
