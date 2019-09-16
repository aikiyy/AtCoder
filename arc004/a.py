from itertools import combinations
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for xy1, xy2 in combinations(XY, 2):
    num = ((xy1[0] - xy2[0])**2 + (xy1[1]-xy2[1])**2)**0.5
    ans = max(ans, num)
print(ans)
