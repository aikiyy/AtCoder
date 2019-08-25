abc = list(map(int, input().split()))
k = int(input())


max_num = max(abc)
abc.remove(max_num)
print(sum(abc) + max_num * 2 ** (k))