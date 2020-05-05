def pagesNumberingWithInk(current, numberOfDigits):
    arr = ''

    while len(arr) < numberOfDigits:
        arr += str(current)
        current += 1
    
    if len(arr) > numberOfDigits:
        return current - 2
    
    return current - 1
