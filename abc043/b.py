ans = ''
for s in input():
    if s in ['0', '1']:
        ans = ans + s
    else:
        if ans != '':
            ans = ans[:-1]
print(ans)
