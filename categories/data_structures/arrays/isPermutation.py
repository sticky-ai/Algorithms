def isPermutation(n, inputArray):
    return sorted(inputArray) == list(range(1, n+1))
