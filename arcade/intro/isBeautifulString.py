def isBeautifulString(inputString):
    alphabet = string.ascii_lowercase
    counted = [inputString.count(i) for i in alphabet]
    #print(counted[::-1])
    #print(sorted(counted))
    return counted[::-1] == sorted(counted)
