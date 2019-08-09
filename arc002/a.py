y = int(input())
print('YES' if y%4 == 0 and (y%400 == 0 or y%100 != 0) else 'NO')