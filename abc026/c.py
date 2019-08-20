n = int(input())
edges = [set() for _ in range(n)]
for a in range(1, n):
    b = int(input())
    edges[b-1].add(a)


def calc_salary(x):
    if len(edges[x]) == 0:
        return 1
    sub_x = [calc_salary(y) for y in edges[x]]
    return max(sub_x) + min(sub_x) + 1


print(calc_salary(0))
