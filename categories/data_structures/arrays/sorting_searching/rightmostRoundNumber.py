def rightmostRoundNumber(inputArray):
    cnt = -1
    for i in range(len(inputArray)):
        if inputArray[i] % 10 == 0:
            cnt = i
    return cnt
