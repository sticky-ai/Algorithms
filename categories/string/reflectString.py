def reflectString(inputString):
    return ''.join([chr(25 - (ord(i) - 97) + 97) for i in inputString])
