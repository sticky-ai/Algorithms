def houseNumbersSum(inputArray):
    temp = 0
    for i in inputArray:
        if i == 0:
            return temp
        temp += i
    return temp
