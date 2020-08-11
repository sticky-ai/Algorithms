def arrayConversion(inputArray):
    while True:
        if len(inputArray) == 1:
            return sum(inputArray)
        else:
            inputArray = [inputArray[i] + inputArray[i+1] for i in range(0, len(inputArray) - 1, 2)]
            if len(inputArray) >= 2:
                inputArray = [inputArray[i] * inputArray[i+1] for i in range(0, len(inputArray) - 1, 2)]
        
