a, b = map(int, input().split())
AB = str(a) * b
BA = str(b) * a
print(AB if AB < BA else BA)
