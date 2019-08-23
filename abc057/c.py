N = int(input())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
    return divisors


def F(a, b):
    return max(len(str(a)), len(str(b)))


ans = []
for n in make_divisors(N):
    n2 = N // n
    ans.append(F(n, n2))
print(min(ans))
