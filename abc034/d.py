def calc(c):
    salt_list = []
    for w, p in WP:
        salt_list.append(w * (p - c) / 100)
    salt_list = sorted(salt_list, reverse=True)
    if sum(salt_list[:K]) >= 0:
        return True
    else:
        return False


N, K = map(int, input().split())
WP = [list(map(int, input().split())) for _ in range(N)]
l = 0
r = 100
_mid = 0
while True:
    mid = (r + l) / 2
    if calc(mid):
        l = mid
    else:
        r = mid
    if mid == _mid:
        break
    else:
        _mid = mid
print(mid)
