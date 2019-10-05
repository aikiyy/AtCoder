D = list(map(int, input().split()))
J = list(map(int, input().split()))
print(sum(max(i) for i in zip(D, J)))
