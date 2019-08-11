n = int(input())
w = input()[:-1].split(' ')
l = [
    'TAKAHASHIKUN',
    'Takahashikun',
    'takahashikun'
]
print(sum([w.count(i) for i in l]))