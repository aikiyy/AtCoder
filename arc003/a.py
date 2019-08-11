n = int(input())
s = input()
sum = s.count('A') * 4 + s.count('B') * 3 + s.count('C') * 2 \
    + s.count('D')
print(sum/n)