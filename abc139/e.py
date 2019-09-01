N = int(input())
A = [list(map(lambda x: int(x)-1, input().split())) for _ in range(N)]
ans = 0
match_users = list(range(N))
while True:
    skip_list = set()
    for i in match_users:
        opp = A[i][0]
        if i in skip_list or opp in skip_list:
            continue
        if A[opp][0] == i:
            skip_list.add(A[opp].pop(0))
            skip_list.add(A[i].pop(0))
            if len(A[i]) == 0:
                match_users.remove(i)
            if len(A[opp]) == 0:
                match_users.remove(opp)
    if len(skip_list) == 0:
        print(-1)
        exit()
    ans += 1
    if len(match_users) == 0:
        break
print(ans)
