n = int(input())
t = [int(input()) for _ in range(n)]
ans = []
for i in range(2**n):
    u = list(map(int, bin(i)[2:].zfill(n)))
    ans.append(max(sum(map(lambda x, y: x if y == 1 else 0, t, u)), sum(map(lambda x, y: x if y == 0 else 0, t, u))))
print(min(ans))
