n, q = map(int, input().split(' '))
s = input()
c = [0] * n
for i in range(1, n):
    c[i] += c[i-1]
    if s[i-1:i+1] == 'AC':
        c[i] += 1
for _ in range(q):
    l, r = map(int, input().split(' '))
    print(c[r-1] - c[l-1])
