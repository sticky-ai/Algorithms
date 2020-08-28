def reverseInteger(x):
    return int(str(x)[::-1]) if x > 0 else int('-' + str(abs(x))[::-1])
