c1, c2 = [input() for _ in range(2)]
print('YES' if c1 == c2[::-1] else 'NO')