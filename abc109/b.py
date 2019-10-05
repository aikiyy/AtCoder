N = int(input())
words = set()
_w = input()
words.add(_w)
for _ in range(N-1):
    w = input()
    if w not in words and _w[-1] == w[0]:
        words.add(w)
        _w = w
        continue
    print('No')
    exit()
print('Yes')
