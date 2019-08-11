s = input()

i = len(s) - 2
while True:
    s = s[:i]
    if s[:i//2] == s[i//2:]:
        break
    i -= 2
print(i)