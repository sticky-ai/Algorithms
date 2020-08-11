def minimalNumberOfCoins(coins, price):
    cnt = 0
    for c in coins[::-1]:
        cnt += price // c
        price -= c * (price // c)
        if price == 0:
            break
    return cnt
