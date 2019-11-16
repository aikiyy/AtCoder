from itertools import permutations
import math

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
ans_list = []
for i in permutations(range(N)):
    ans = 0
    for j in range(N-1):
        ans += math.sqrt((XY[i[j]][0] - XY[i[j+1]][0])**2 + (XY[i[j]][1] - XY[i[j+1]][1])**2)
    ans_list.append(ans)
print(sum(ans_list)/len(ans_list))
