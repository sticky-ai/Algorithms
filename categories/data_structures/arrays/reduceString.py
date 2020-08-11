def reduceString(inputString):
    inputString = list(inputString)
    while True:
        try:
            if inputString[0] == inputString[-1] and len(inputString) > 1:
                inputString.pop(0)
                inputString.pop()
            else:    
                return ''.join(inputString) if len(inputString) > 1 else ''
        except:
            return ''
