def isTandemRepeat(inputString):
    center = int(len(inputString) / 2)
    return inputString[:center] == inputString[center:]



