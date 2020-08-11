def sumUpNumbers(inputString):
    r = re.split('[^\d]', inputString)
    return sum([int(i) for i in r if i.isdigit() is True])
