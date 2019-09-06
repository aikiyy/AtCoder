N = int(input())
if N == 1:
    flag = False
elif all([N % i != 0 for i in range(2, int(N**0.5)+1)]):
    flag = True
elif N % 2 != 0 and N % 5 != 0 and N % 3 != 0:
    flag = True
else:
    flag = False
print('Prime' if flag else 'Not Prime')
