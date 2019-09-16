from itertools import combinations

nums = list(map(int, input().split()))
ans = []
for a in combinations(nums, 3):
    ans.append(sum(a))
print(sorted(ans)[-3])
