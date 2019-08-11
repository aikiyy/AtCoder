s = input()
n = int(input())
print(len(set([s[i:i+n] for i in range(len(s) - n + 1)])))
