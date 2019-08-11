n = int(input())
s = input()
c = [s.count(i) for i in map(str, range(1, 5))]
print(max(c), min(c))