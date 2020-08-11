def depositProfit(deposit, rate, threshold):
    count = 0
    while(1):
        if deposit < threshold:
            deposit += deposit * rate / 100
            count += 1
            
        else:
            return count
