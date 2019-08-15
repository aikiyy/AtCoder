n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

l = []
for i in range(n):
    l.append(sum(a1[0:i+1]) + sum(a2[i:]))

print(max(l))
