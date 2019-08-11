coin = {
    'JPY': 0,
    'BTC': 0
}
for _ in range(int(input())):
    x, u = input().split(' ')
    coin[u] += float(x)
print(coin['JPY'] + coin['BTC'] * 380000)
