n = int(input())
a = list(map(int, input().split()))

print(1 / sum(map(lambda x: 1.0 / x, a)))