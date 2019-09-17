N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(M)]
for a, b in AB:
    dis = float('inf')
    for i, cd in enumerate(CD):
        now_dis = abs(a - cd[0]) + abs(b - cd[1])
        if now_dis < dis:
            dis = now_dis
            checkpoint = i+1
    print(checkpoint)
