import bisect


N = int(input())
C = [int(input()) for _ in range(N)]


LIS = [C[0]]
for i in range(1, N):
    # LISの最後尾より大きいならそのまま追加
    if C[i] > LIS[-1]:
        LIS.append(C[i])
    # そうじゃないならその値を入れられるindexを変更
    else:
        LIS[bisect.bisect_left(LIS, C[i])] = C[i]
print(N - len(LIS))
