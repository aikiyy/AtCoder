N = int(input())
P = list(map(int, input().split()))

ans = [0]
for i in range(N):
    next_ans = []
    next_ans.append(P[i])
    for j in ans:
        next_ans.append(j+P[i])
    ans.extend(next_ans)
    ans = list(set(ans))
print(len(ans))
