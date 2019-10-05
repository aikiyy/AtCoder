N = int(input())
A = [a-i-1 for i, a in enumerate(map(int, input().split()))]
A = sorted(A)
print(sum(abs(a - A[N//2]) for a in A))
