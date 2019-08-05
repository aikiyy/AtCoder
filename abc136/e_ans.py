# -*- coding: utf-8 -*-


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return sorted(divisors, reverse=True)


if __name__ == '__main__':
    n, k = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    divisors = make_divisors(sum(A))
    for divisor in divisors:
        remainders = sorted(map(lambda x: x % divisor, A))
        idx = n - sum(remainders) // divisor
        ope_num = sum(remainders[:idx])
        if ope_num <= k:
            print(divisor)
            break
