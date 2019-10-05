N = int(input())
A = []
for i, v in enumerate(list(map(int, input().split()))):
    A.append((i+1, v))
for v in sorted(A, key=lambda x: x[1], reverse=True):
    print(v[0])
