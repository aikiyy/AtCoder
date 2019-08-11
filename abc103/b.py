s, t = [input() for _ in range(2)]
for i in range(len(s)):
    if s[i:] + s[:i] == t:
        print('Yes')
        break
else:
    print('No')