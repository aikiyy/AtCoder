def is_prime(n):
    '''
    素数判定する
    '''
    if n == 1:
        return False
    for k in range(2, int(n**0.5) + 1):
        if n % k == 0:
            return False
    return True


N = int(input())
ans = 0
for i in range(2, N):
    if is_prime(i):
        ans += 1
print(ans)