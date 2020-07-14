def addBinaryStrings(a, b):
    if a and b:
        return str(bin(int('0b' + a, 2) + int('0b' + b, 2)))[2:]
    return a if a else b
