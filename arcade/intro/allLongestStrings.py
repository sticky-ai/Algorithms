def allLongestStrings(inputArray):
    length = max([len(i) for i in inputArray])
    return [i for i in inputArray if len(i) == length]
