from itertools import groupby

S = input()
N = int(input())

if len(S) == 1:
    print(N//2)
    exit()

if len(S) == 2 and S[0] == S[1]:
    print(N)
    exit()

check = S
check_num = sum(len(list(v))//2 for k, v in groupby(check))
check2 = S * 2
check2_num = sum(len(list(v))//2 for k, v in groupby(check2))
check3 = S * 3
check3_num = sum(len(list(v))//2 for k, v in groupby(check3))
check4 = S * 4
check4_num = sum(len(list(v))//2 for k, v in groupby(check4))

if N % 2 == 0:
    print(check2_num + (check4_num-check2_num)*(N//2-1))
else:
    print(check_num + (check3_num-check_num)*(N//2))
