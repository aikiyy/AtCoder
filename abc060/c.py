N, time = map(int ,input().split())
T = list(map(int ,input().split()))


ans = 0
start_time = T[0]
end_time = T[0] + time
for i in range(1, N):
    if T[i] <= end_time:
        ans += T[i] - start_time
        start_time = T[i]
        end_time = T[i] + time
    else:
        ans += time
        start_time = T[i]
        end_time = T[i] + time
ans += time


print(ans)
