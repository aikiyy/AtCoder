import math


def find_root(arr, src):
    arr.append(src)
    if src == 0:
        return arr
    else:
        return find_root(arr, upper_edge[src])


def find_end(arr, src):
    if len(under_edge[src]) == 0:
        return arr
    else:
        max([find_end([arr.append(src)], e) for e in under_edge[src]])



N, u, v = map(int, input().split())
u -= 1
v -= 1
under_edge = [[] for _ in range(N)]
upper_edge = [0] * N
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a < b:
        under_edge[a].append(b)
        upper_edge[b] = a
    else:
        under_edge[b].append(a)
        upper_edge[a] = b

print(find_end(u, v))
u_path = find_root([], u)
v_path = find_root([], v)
both = set(u_path) & set(v_path)
both_number = max(both)
u_idx = u_path.index(both_number)
v_idx = v_path.index(both_number)
print(u_path, v_path)
print(u_idx, v_idx)
print(math.ceil((max(u_idx, v_idx) - min(u_idx, v_idx))/2))
