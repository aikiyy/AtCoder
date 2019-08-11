s = input()
for _ in range(int(input())):
    l, r = map(int, input().split(' '))
    l = l-1
    s = s[:l] + s[l:r][::-1] + s[r:]
print(s)