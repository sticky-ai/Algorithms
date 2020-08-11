def deleteDigit(n):
    num = str(n)
    return max([int(num[:i] + num[i+1:]) for i in range(len(num))])
