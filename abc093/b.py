a, b, k = map(int, input().split(' '))
A = list(filter(lambda x: x <= b, [i for i in range(a, a+k)]))
B = list(filter(lambda x: x >= a, [i for i in range(b-k+1, b+1)]))
print('\n'.join(map(str, sorted(list(set(A+B))))))
