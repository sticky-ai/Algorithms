def maxSumWithoutAdjacents(a):
    preMax, curMax = 0, 0
    for n in a:
        m = max(curMax, preMax + n)
        preMax, curMax = curMax, m
    return curMax
