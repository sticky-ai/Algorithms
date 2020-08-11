def alphabeticShift(inputString):

    lst = ['a' if inputString[i] == 'z' else chr(ord(inputString[i])+1) for i in range(len(inputString))]
    return ''.join(lst)

