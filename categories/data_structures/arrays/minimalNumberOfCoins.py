def minimalNumberOfCoins(coins, price):
    cnt = 0
    for c in coins[::-1]:
        cnt += price // c
        price -= (price // c) * c
    return cnt
