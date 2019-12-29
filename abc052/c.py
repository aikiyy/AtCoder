from collections import defaultdict


def trial_division(n):
    '''
    素因数分解する
    '''
    factor = []
    for num in range(2, int(n**0.5)+1):
        while n % num == 0:
            n //= num
            factor.append(num)
    if not factor or n != 1:
        factor.append(n)
    return factor


N = int(input())
divisor_dict = defaultdict(int)
for i in range(2, N+1):
    divisors = trial_division(i)
    for d in divisors:
        divisor_dict[d] += 1
ans = 1
for v in divisor_dict.values():
    ans = (ans * (v+1)) % (1e9 + 7)
print(int(ans))