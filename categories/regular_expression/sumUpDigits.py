def sumUpDigits(inputString):
    return sum(map(int, re.findall('[0-9]', inputString)))
