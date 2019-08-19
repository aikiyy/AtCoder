from queue import Queue


R, C = map(int, input().split())
s = list(map(int, input().split()))
g = list(map(int, input().split()))
cc = ['#' + input() + '#' for _ in range(R)]
cc.insert(0, '#'*(C+2))
cc.append('#'*(C+2))

q = Queue()
q.put(s)
costs = [[-1] * (C+1) for _ in range(R+1)]
costs[s[0]][s[1]] = 0
while not q.empty():
    now = q.get()
    r, c = now
    for rc in [[r-1, c], [r, c-1], [r, c+1], [r+1, c]]:
        if cc[rc[0]][rc[1]] == '.':
            if costs[rc[0]][rc[1]] == -1:
                costs[rc[0]][rc[1]] = costs[r][c] + 1
                q.put(rc)

print(costs[g[0]][g[1]])
