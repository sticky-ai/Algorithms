def arrayMaxConsecutiveSum2(inputArray):
    currentSum = 0
    maxSum = max(inputArray)
    for i in range(len(inputArray)):
        currentSum = max(inputArray[i] + currentSum, inputArray[i])
        maxSum = max(currentSum, maxSum)
    return maxSum

    # ans = set()
    # for i in range(1, len(inputArray) + 1):
    #     for j in range(len(inputArray)):
    #         ans.add(tuple(inputArray[j:j+i]))
    # return max(map(sum, ans))
