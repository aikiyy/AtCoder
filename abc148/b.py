N = int(input())
S, T = input().split()

print(''.join([i+j for i, j in zip(S, T)]))
