a, b, c, x = [int(input()) for _ in range(4)]
ans = 0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if i*500+j*100+k*50 == x:
                ans += 1
print(ans)