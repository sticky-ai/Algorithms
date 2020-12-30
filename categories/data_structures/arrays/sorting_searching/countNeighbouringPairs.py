def countNeighbouringPairs(inputString):
    return sum([1 for i in range(len(inputString) - 1) if inputString[i] == inputString[i+1]])
