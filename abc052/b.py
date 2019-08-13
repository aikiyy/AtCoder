n = int(input())
S = input()

ans = 0
_ans = 0
for s in S:
    if s == 'I':
        _ans += 1
    else:
        _ans -= 1
    ans = max(ans, _ans)
print(ans)
