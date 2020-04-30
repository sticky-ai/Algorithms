def arrayMaxConsecutiveSum(inputArray, k):
    inputArray.sort(reverse = True)

    return sum(inputArray[:k])

