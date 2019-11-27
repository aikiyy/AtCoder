import bisect


N = int(input())
LR = []
for _ in range(N):
    x, r = map(int, input().split())
    LR.append((x-r, x+r))
LR = sorted(LR, key=lambda x: (x[1], x[0]), reverse=True)

LIS = [LR[0][0]]
for i in range(1, N):
    if LR[i][0] > LIS[-1]:
        LIS.append(LR[i][0])
    else:
        LIS[bisect.bisect_left(LIS, LR[i][0])] = LR[i][0]
print(len(LIS))
