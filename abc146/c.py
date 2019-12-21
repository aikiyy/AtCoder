A, B, X = map(int, input().split())

lower = 0
upper = X
_ans = (lower + upper) // 2
ans = _ans
while True:
    if A * ans + B * len(str(ans)) <= X:
        lower = ans
    else:
        upper = ans
    ans = (lower + upper) // 2
    if ans == _ans:
        break
    _ans = ans
print(min(ans, pow(10, 9)))
