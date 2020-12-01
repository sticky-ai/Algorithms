def countDistantPairs(inputString, distance):
    cnt = 0
    for i in range(len(inputString)):
        for j in range(i+1, len(inputString)):
            if inputString[i] == inputString[j] and j - i - 1 == distance:
                cnt += 1
                
    return cnt
