def isTandemRepeat(inputString):
    return len(inputString) % 2 == 0 and len(inputString) // len(set(inputString)) == 2
