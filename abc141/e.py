import math


N = int(input())
S = input()


def check(length_s):
    for start_s in range(0, N-length_s):
        check_s = S[start_s:start_s+length_s]
        if length_s > N - start_s - length_s:
            break
        if check_s in S[start_s+length_s:]:
            return True
    return False


max_s = N // 2
length_s = N // 2 // 2
min_s = 0
while True:
    print(length_s, max_s, min_s)
    if check(length_s):
        min_s = length_s
        length_s = math.ceil((max_s + length_s) / 2)
    else:
        max_s = length_s
        length_s = math.floor((min_s + length_s) / 2)
    print(length_s, max_s, min_s)
    if length_s == max_s or length_s == min_s:
        break
print(length_s)
