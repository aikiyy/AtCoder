a, b, c, k = map(int, input().split(' '))
s, t = map(int, input().split(' '))


adult = b * t
child = a * s
discount = c * (s + t) if s + t >= k else 0

print(adult + child - discount)