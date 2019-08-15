a = list(map(int, input().split()))
diff_a = sum(map(lambda x: max(a) - x, a))
if diff_a % 2 == 0:
    print(diff_a // 2)
else:
    print(diff_a // 2 + 2)

