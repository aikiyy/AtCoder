R, B = map(int, input().split())
X, Y = map(int, input().split())


l = 0
r = min(R, B) + 1
_taba = 0
while True:
    taba = (l + r) // 2
    if (R - taba) // (X - 1) + (B - taba) // (Y - 1) >= taba:
        l = taba
    else:
        r = taba
    if taba == _taba:
        break
    _taba = taba
print(taba)
