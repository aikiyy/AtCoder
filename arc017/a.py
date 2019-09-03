N = int(input())
print('YES' if all([N%int(i) != 0 for i in range(2, int(N**0.5)+1)]) else 'NO')
