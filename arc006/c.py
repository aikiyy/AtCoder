import bisect


N = int(input())
ws = []
for _ in range(N):
    w = int(input())
    idx = bisect.bisect_left(ws, w)
    if idx == len(ws):
        ws.append(w)
    else:
        ws[idx] = w
print(len(ws))
