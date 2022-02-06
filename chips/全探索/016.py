N = int(input())
coins = map(int, input().split())
max_coins = 9999

coins = sorted(coins)
max_coin = coins[2]
min_coin = coins[0]
av_coin = coins[1]

abc = []
for i in range(0, max_coins):
    amari1 = N - (max_coin * i)
    if amari1 < 0:
        break
    if amari1 == 0:
        abc.append(i)
        break
    for j in range(0, max_coins - i):
        amari2 = amari1 - (av_coin * j)
        if amari2 < 0:
            break
        if amari2 == 0:
            abc.append(i + j)
            break

        if amari2 % min_coin == 0:
            abc.append(i + j + amari2 // min_coin)

print(min(abc))
