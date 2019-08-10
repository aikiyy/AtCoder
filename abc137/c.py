n = int(input())
sn = {}
for _ in range(n):
    s = ''.join(sorted(input()))
    sn[s] = sn.get(s, 0) + 1

ans = 0
for k, v in sn.items():
    if v == 1:
        continue
    ans += (v-1) * v / 2

print(int(ans))
