def extractEachKth(inputArray, k):
    return [inputArray[n-1] for i, n in enumerate(range(len(inputArray) + 1)) if i % k != 0]
