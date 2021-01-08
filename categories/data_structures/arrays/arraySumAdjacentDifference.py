def arraySumAdjacentDifference(inputArray):
    return sum(abs(inputArray[i] - inputArray[i+1]) for i in range(len(inputArray) - 1))
