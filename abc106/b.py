def make_divisors(n):
    '''
    nの約数リストを返す
    '''
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0 and i % 2 == 1:
            divisors.append(i)
            if i != n // i and n//i % 2 == 1:
                divisors.append(n//i)
    # divisors.sort()
    return divisors


N = int(input())
ans = 0
for i in range(1, N+1):
    divisors = make_divisors(i)
    if len(divisors) == 8:
        ans += 1
print(ans)
