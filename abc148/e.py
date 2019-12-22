def f(n):
    if n < 2:
        return 1
    return n * f(n-2)


N = int(input())

# 奇数の場合0が登場することはない
if N & 1:
    print(0)
else:
    keta = len(str(N))
    ans = 0
    num_list = [1]
    for i in range(1, keta-1):
        if i == 1:
            num_list.append(num_list[-1] * 10)
        else:
            num_list.append(num_list[-1] * 10 + 1)
        num_list[-1] += i+1
    ans += num_list[-1]
    str_num = str(N//10)[1:]
    for i in range(len(str_num)):
        a = str_num[i]
        ans += num_list[-(i+2)] * int(a)
    print(ans)
