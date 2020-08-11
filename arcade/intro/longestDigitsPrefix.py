def longestDigitsPrefix(inputString):
    digit = []
    if inputString[0].isdigit() is True:
        for i in inputString:
            if i.isdigit() is True:
                digit.append(i)
            else:
                break
    return "".join(digit)



