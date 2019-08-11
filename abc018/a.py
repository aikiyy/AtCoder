s = [int(input()) for _ in range(3)]
sort_s = sorted(s, reverse=True)
for i in s:
    print(sort_s.index(i) + 1)
