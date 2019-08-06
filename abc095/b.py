N, X = map(int, input().split(' '))
d = [int(input()) for _ in range(N)]
print(N + (X-sum(d)) // min(d))
