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


Q = int(input())
prime_list = [False] * 100001
L = []
R = []
for _ in range(Q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
a = [0] * 100001
prime_list[2] = True
for i in range(1, 100001):
    prime_list[i] = is_prime(i)
    if prime_list[i] and prime_list[(i+1)//2]:
        a[i] = a[i-1] + 1
    else:
        a[i] = a[i-1]
for i in range(Q):
    ans = a[R[i]] - a[L[i]-1]
    print(ans)
