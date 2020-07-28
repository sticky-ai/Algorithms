def depositProfit(deposit, rate, threshold):
    cnt = 0
    while deposit < threshold:
        cnt += 1
        deposit *= 1 + (rate * 0.01)
    return cnt
