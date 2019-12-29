A, B, K = map(int, input().split())
a = max(A-K, 0)
b = max(0, B-(K-A)) if A < K else B
print(a, b)
