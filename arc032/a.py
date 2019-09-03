N = int(input())
nsum = (N+1) * N // 2
print('WANWAN' if nsum != 1 and all([nsum % i != 0 for i in range(2, int(nsum**0.5)+1)]) else 'BOWWOW')
