def arrayMaxConsecutiveSum(inputArray, k):
    x = y = 0
    for i in range(len(inputArray) - k + 1):
        x = y
        y = max(x, sum(inputArray[i:i+k]))
    return y
