N = int(input())
edge = []
# bとして振られる番号
d_col = [0] * N
# b先に振り分ける番号
e_col = [1] * N
for i in range(N-1):
    a, b = map(int, input().split())
    edge.append([a, b, i, 0])
edge = sorted(edge)
for j, e in enumerate(edge):
    a, b, i, ans = e
    if d_col[a-1] == e_col[a-1]:
        edge[j][3] = e_col[a-1] + 1
        e_col[a-1] += 1
    else:
        edge[j][3] = e_col[a-1]
    d_col[b-1] = e_col[a-1]
    e_col[a-1] += 1
edge = sorted(edge, key=lambda x: x[2])
col = []
for e in edge:
    col.append(e[3])
print(max(col))
for i in col:
    print(i)
