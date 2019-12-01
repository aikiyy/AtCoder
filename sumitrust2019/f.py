import math


T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

# T1,T2以内に出会えるか, 出会えないなら一生無理
x = (T1*B1 - T1*A1) / (A2 - B2)
if x < 0 or x > T2:
    print(0)
    exit()

times = [T1+x]
dis_a = T1*A1 + T2*A2
dis_b = T1*B1 + T2*B2
T = T1 + T2
# T3で出会うか
x = (dis_b - dis_a) / (A1 - B1)
if 0 < x <= T1:
    times.append(T + x)

# T4で出会うか
x = (dis_b + T1*B1 - dis_a - T1*A1) / (A2 - B2)
if 0 < x <= T2:
    times.append(T + T1 + x)

# T5で出会うか
x = (dis_b*2 - dis_a*2) / (A1 - B1)
if 0 < x <= T1:
    times.append(T*2 + x)

# T6で出会うか
x = (dis_b*2 + T1*B1 - dis_a*2 - T1*A1) / (A2 - B2)
if 0 < x <= T2:
    times.append(T*2 + T1 + x)

## T7で出会うか
#x = (dis_b*3 - dis_a*3) / (A1 - B1)
#if 0 < x <= T1:
#    times.append(T*3 + x)
#
## T8で出会うか
#x = (dis_b*3 + T1*B1 - dis_a*3 - T1*A1) / (A2 - B2)
#if 0 < x <= T2:
#    times.append(T*3 + T1 + x)

dis_times = []
for i in range(len(times)-1):
    dis_times.append(times[i+1] - times[i])

if len(dis_times) == 0:
    print(len(times))
    exit()
if dis_times[0] == dis_times[1]:
    print('infinity')
    exit()
if dis_times[1] > dis_times[3]:
    x = dis_times[1] / (dis_times[1] - dis_times[3])
    print(math.ceil(x*2)+1)
    exit()
else:
    x = dis_times[0] / (dis_times[0] - dis_times[2])
    print(math.ceil(x*2))
    exit()
