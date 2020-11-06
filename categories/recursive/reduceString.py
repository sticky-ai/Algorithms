def reduceString(inputString):
    if len(inputString) < 2:
        return ''
    if inputString[0] == inputString[-1]:
        return reduceString(inputString[1:-1])
    return inputString
