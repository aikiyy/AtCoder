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


X = int(input())
i = X
while True:
    if is_prime(i):
        print(i)
        break
    else:
        i += 1
