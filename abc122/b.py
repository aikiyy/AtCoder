S = input()
acgt = ['A', 'C', 'G', 'T']
ans = 0
_ans = 0
for s in S:
    if s in acgt:
        _ans += 1
    else:
        _ans = 0
    ans = max(ans, _ans)
print(ans)
