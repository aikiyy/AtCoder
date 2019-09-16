N = int(input())


def trial_division(n):
    factor = []
    for num in range(2, int(n**0.5)+1):
        while n % num == 0:
            n //= num
            factor.append(num)
    if not factor or n != 1:
        factor.append(n)
    return factor


d = {}
for i in range(2, N+1):
    divisors = trial_division(i)
    for divisor in divisors:
        d[divisor] = d.get(divisor, 0) + 1

ans = 1
for v in d.values():
    ans = ans * (v + 1) % (10**9+7)
print(ans)
